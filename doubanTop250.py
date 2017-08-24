#-*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
import time
import sys

def getHTMLText(url,k):
    try:
        if(k==0):kw={}
        else:kw={'start':k,'filter':''}
        r=requests.get(url,params=kw,headers={'User-Agent':'Mozilla/4.0'})
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        print("Faided!")
def getData(html):
    soup=BeautifulSoup(html,"html.parser")
    movieList=soup.find('ol',attrs={'class':'grid_view'})
    moveInfo=[]
    for movieLi in movieList.find_all('li'):
        data=[]
        movieHd=movieLi.find('div',attrs={'class':'hd'})
        movieName=movieHd.find('span',attrs={'class':'title'}).getText()

        data.append(movieName)

    print(outputMode.format(data[0]))

output=sys.stdout
outputfile=open("moviedata.txt",'w')
sys.stdout=outputfile



outputMode="{0:{4}^20}\t{1:^10}\t{2:^10}\t{3:{4}<10}"

basicURL='http://movie.douban.com/top250'
k=0
while k<=225:
   html=getHTMLText(basicURL,k)
   time.sleep(2)
   k+=25
   getData(html)

outputfile.close()
sys.stdout=output
