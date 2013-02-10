#!/usr/bin/python

import codecs
import re
import markdown
import sys

if not sys.argv[:2]:
    exit()

content_file = sys.argv[1]

header = codecs.open('parts/header.html', mode = 'r', encoding = 'utf-8')
header = header.read()

footer = codecs.open('parts/footer.html', mode = 'r', encoding = 'utf-8')
footer = footer.read()

content = codecs.open(content_file, mode = 'r', encoding = 'utf-8')
content = content.read()
content = markdown.markdown(content)

rules = [
    ['<h([0-9])>(.*?)</h([0-9])>', '<div class="slide"><div class="slide-inner"><h\\1 class="animate-in" data-animation="fly-in-left">\\2</h\\3></div></div>'],
    ['<p><img(.*?)</p>', '<div class="slide slide-image"><div class="slide-inner"><p class="animate-in"><img\\1</p></div></div>'],
    ['<p>(.*?)</p>', '<div class="slide"><div class="slide-inner"><p class="animate-in">\\1</p></div></div>']
]

for pattern, replace in rules:
    content = re.sub(pattern, replace, content, flags = re.MULTILINE | re.DOTALL)

output = '%s%s%s' % (header, content, footer)
print output.encode('utf-8')
