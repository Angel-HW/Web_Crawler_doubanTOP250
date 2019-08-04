import urllib.request
import re

url = 'https://movie.douban.com/top250'
req = urllib.request.urlopen(url)
html = req.read().decode('utf-8')

tit = r'<span class="title">[^"]+</span>'
titlelist = re.findall(tit,html)

print(len(titlelist))

for ench in titlelist:
    print(ench)
