import urllib.request
import re

name = 1
for ench in range(0,250,25):
    url = 'https://movie.douban.com/top250?start='+str(ench)+'&filter='
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36')
    req = urllib.request.urlopen(req)
    html = req.read().decode('utf-8')

    tit = r'<img width="100" alt="(.*)" src="([^"]+\.jpg)" class="">+(?:[\s\S]*?)+<span class="rating_num" property="v:average">+(\d\.\d)+</span>+(?:[\s\S]*?)+<span>+([\d]+人评价)+</span>'
    titlelist = re.findall(tit,html)
    for ench in titlelist:
        print(name,ench)
        name+=1
