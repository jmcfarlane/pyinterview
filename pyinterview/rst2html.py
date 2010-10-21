# Third party imports
from docutils import core

def rst2html(rst):
    parts = core.publish_parts(source=rst, writer_name='html')
    return ''.join((parts['body_pre_docinfo'],  parts['fragment']))
