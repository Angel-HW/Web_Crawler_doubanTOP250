import urllib.request
import re
import urllib.error
import socket
import time

start = time.perf_counter()

socket.setdefaulttimeout(10)

def get_html(url):
    try:
        req = urllib.request.Request(url)
        req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36')
        req = urllib.request.urlopen(req)
        html = req.read().decode('utf-8')
        return html
    except error.HTTPError as e:
        print(e.reason,e.code)
    except error.URLError as e:
        print(e.reason)

def download_img(picture_url,file_name,name):#保存海报
    try:
        urllib.request.urlretrieve(picture_url,file_name,None)
        print('爬了'+str(name)+'张')
        '''
        print(pictrue_url,pictrue_name)
        name+=1
        print(name,ench)
        '''
    except socket.timeout:
        count = 1
        while count < 3:
            try:
                print('第'+str(count)+'次失败！')
                urllib.request.urlretrieve(picture_url,file_name,None)
                print('爬了'+str(name)+'张')
                break
            except socket.timeout:
                count+=1
        if count > 3:
            print('爬取失败！')
    return name

def get_info(ench,name):#保存信息
    file = open(r'E:\Study\programingtools\py\program\doubanTOP250\infomation\info.txt','a')
    for en in ench:
        data = {
            '排名：':name,
            '剧名：':ench[0],
            '海报链接：':ench[1],
            '评分：':ench[2]+'分',
            '评论人数：':ench[3]
            }
        file.write(str(data))
    file.write('\n')
    print(name,ench)
    if file:
        file.close()

def get_img(html,name):#得到海报链接
    tit = r'<img width="100" alt="(.*)" src="([^"]+\.jpg)" class="">+(?:[\s\S]*?)+<span class="rating_num" property="v:average">+(\d\.\d)+</span>+(?:[\s\S]*?)+<span>+([\d]+人评价)+</span>'
    titlelist = re.findall(tit,html)
    for ench in titlelist:
        pictrue_url = ench[1]
        pictrue_name = ench[0]
        file_name = 'E:\Study\programingtools\py\program\doubanTOP250\picture\\'+str(name)+'_'+pictrue_name+'.jpg'
        get_info(ench,name)
        name = download_img(pictrue_url,file_name,name)
        name += 1
    return name
        
if __name__=='__main__':
    print('正在爬取，请稍后……')
    name = 1
    for ench in range(0,250,25):
        url = 'https://movie.douban.com/top250?start='+str(ench)+'&filter='
        name = get_img(get_html(url),name)
    print('图片爬取成功！')
    use_time = (time.perf_counter() - start)
    print('总共用时：',use_time)
