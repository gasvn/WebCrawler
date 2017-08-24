# -*- coding:utf-8 -*-
import urllib
import urllib.request
import re
def download_page(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) ''AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}
    request = urllib.request.Request(url,headers=headers)
    response=urllib.request.urlopen(request)
    data=response.read()
    return data

def get_image(html):
    regx=r'http://[\S]*\.jpg'
    patten=re.compile(regx)
    get_img=re.findall(patten,repr(html))
    num=1
    for img in get_img:
        image=download_page(img)
        with open('%s.jpg'%num,'wb') as fp:
            fp.write(image)
            num+=1
            print('正在下载中的第%s张图片'%num)
    return
url='http://pic.yesky.com/451/106166451.shtml'
html=download_page(url)
get_image(html)
