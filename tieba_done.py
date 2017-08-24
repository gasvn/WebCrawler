# -*- coding:utf-8 -*-
import re
import urllib.request

def getHtml(url):
    page=urllib.request.urlopen(url)
    html=page.read()
    return html

#html=getHtml("http://tieba.baidu.com/p/3205263090")
html=getHtml("https://tieba.baidu.com/p/5256331871")
html=html.decode('UTF-8')# 把html文件格式改成UTF-8

def getImg(html):
    #reg=r'src="([.*\S]*\.jpg)" pic_ext="jpeg"'
    reg=r'src="([.*\S]*\.jpg)" size'# 正则不等式
    imgre=re.compile(reg)
    imglist=re.findall(imgre,html)
    return imglist

imgList=getImg(html)
imgName=50
for imgPath in imgList:
    f=open("image/"+str(imgName)+".jpg",'wb')
    f.write((urllib.request.urlopen(imgPath)).read())
    f.close()
    imgName+=1
print("OK")
