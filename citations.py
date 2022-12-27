from distutils.filelist import findall
import string
from nbformat import read
import requests, re
from bs4 import BeautifulSoup


citation_site = requests.get('https://www.quotesandthoughts.com/stoic-quotes/')

result = BeautifulSoup(citation_site.text, 'html.parser')

# body = result.body
# bcontent = body.contents

# print(bcontent[15].next_sibling)

citations = result.find_all(attrs={'style':'font-size: 14pt; color: #000000;'})


list_citations = list(citations)

# store in a file
f = open('citations.txt', 'w')

for c in citations:
    f.write(c.get_text()+'\n')

f.close()

# f = open('citations.txt', 'r')
# print(f.read())

# quotes = {}
# pattern = re.compile(r'\.\s[A-Z]\w+\s[A-Z]\w+')

# for c in citations:
#     print(pattern.findall(c.get_text()))


