def rot13(msg):
    s = 'abcdefghijklmnopqrstuvwxyz'
    length = len(s)

    output = []
    for c in msg:
        if c in s:
            j = (s.find(c) + (length / 2)) % length
            output.append(s[j])
        else:
            output.append(c)

    return ''.join(output)

text = 'pyinterview'
ecrypted = rot13(text)
print 'Input:', text
print 'Encrypted: [%s]' % ecrypted
print 'Decrypted: [%s]' % rot13(ecrypted)
