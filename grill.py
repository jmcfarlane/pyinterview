# Python imports
import datetime
import optparse
import os
import random
import re
import shutil
import sys
import webbrowser

# Pyinterview imports
import pyinterview

DATE_FORMAT = '%m/%d/%Y %H:%M:%S'
DEFAULT_TEMPLATE = 'templates/question.tmpl'
DEST_DIR = 'pyinterview'
FILE_NAME = 'question_%s.html'
PROMPT = 'Would you like another question? '
QUESTIONS_DIR = 'questions'

def fetch_questions(options):
    re_filter = re.compile(options.filter, re.I | re.M)
    cwd = os.getcwd()
    files = [f for f in os.listdir(QUESTIONS_DIR) if f.endswith('.rst')]
    random.shuffle(files)
    for count, f in enumerate(files):
        contents = open(os.path.join(cwd, QUESTIONS_DIR, f)).read()
        if re_filter.search(contents) or re_filter.search(f):
            print 'Processing:', f
            yield contents

    # Include a congratulations page
    yield open(os.path.join(cwd, 'templates', 'finished.rst')).read()

def getopts():
    p = optparse.OptionParser('Usage: %prog [options]')
    p.add_option('-b', '--browser', dest='browser', action='store_true')
    p.add_option('-d', '--output-dir', dest='dest_dir', type='str')
    p.add_option('-f', '--filter', dest='filter', type='str')

    # Default values
    p.set_defaults(browser=False)
    p.set_defaults(filter='.*')
    p.set_defaults(dest_dir='/tmp')

    options, args = p.parse_args()
    options.dest_dir = os.path.join(options.dest_dir, DEST_DIR)

    return (options, args)

def persist_html(html, count, options):
    path = os.path.join(options.dest_dir, FILE_NAME % count)
    fh = open(path, 'w')
    fh.write(html)
    fh.close()
    
def render_question(rst, template, count):
    model = {}
    model['body'] = pyinterview.rst2html(rst)
    model['now'] = datetime.datetime.now().strftime(DATE_FORMAT)
    model['version'] = pyinterview.version
    model['count'] = count

    if 'Congratulations' in model['body']:
        model['next'] = 'http://github.com/jmcfarlane/pyinterview'
    else:
        model['next'] = FILE_NAME % (count + 1)

    return template % model

def setup_base_dir(path):
    if os.path.exists(path):
        shutil.rmtree(path)

    os.mkdir(path)
    
def main():
    options, args = getopts()
    template = open(DEFAULT_TEMPLATE).read()
    setup_base_dir(options.dest_dir)

    # Loop over and persist questions
    count = 0
    for question in fetch_questions(options):
        count += 1
        html = render_question(question, template, count)
        persist_html(html, count, options)

    print 'Files written to:', options.dest_dir
    if options.browser:
        webbrowser.open('file://%s/question_1.html' % options.dest_dir)

if __name__ == '__main__':
    main()
