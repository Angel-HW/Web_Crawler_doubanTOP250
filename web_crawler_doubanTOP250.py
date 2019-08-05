import urllib.request
import re

url = 'https://movie.douban.com/top250'
req = urllib.request.urlopen(url)
html = req.read().decode('utf-8')

tit = r'<img width="100" alt="(.*)" src="([^"]+\.jpg)" class="">+(?:[\s\S]*?)+<span class="rating_num" property="v:average">+(\d\.\d)+</span>+(?:[\s\S]*?)+<span>+([\d]+人评价)+</span>'
titlelist = re.findall(tit,html)

for ench in titlelist:
    print(ench)
