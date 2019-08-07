import urllib.request
import re

def get_html(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36')
    req = urllib.request.urlopen(req)
    html = req.read().decode('utf-8')
    return html

def download_img(html):
    tit = r'<img width="100" alt="(.*)" src="([^"]+\.jpg)" class="">+(?:[\s\S]*?)+<span class="rating_num" property="v:average">+(\d\.\d)+</span>+(?:[\s\S]*?)+<span>+([\d]+人评价)+</span>'
    titlelist = re.findall(tit,html)
    for ench in titlelist:
        pictrue_url = ench[1]
        pictrue_name = ench[0]
        file_name = 'E:\Study\programingtools\py\program\doubanTOP250\\'+pictrue_name+'.jpg'
        urllib.request.urlretrieve(pictrue_url,file_name,None)
'''
        print(pictrue_url,pictrue_name)
        print(name,ench)
        name+=1
'''
if __name__=='__main__':
    print('正在爬取，请稍后……')
    name = 1
    for ench in range(0,250,25):
        url = 'https://movie.douban.com/top250?start='+str(ench)+'&filter='
        download_img(get_html(url))
    print('图片爬取成功！')
