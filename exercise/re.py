#! /usr/bin/env python
#coding=utf-8

import re
import urllib


ss="010-12345678"
pat='\d{3}-\?\d{8}'
re.findall(pat,ss)



def getHtml(url):
    f=urllib.urlopen(url)
    html=f.read()
    return html






def getIMG(html):
    #reg = r'scr="(.+?\.jpg)" pic_ext '
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist=re.findall(imgre,html)
    print imglist
    x=1
    for i in imglist:
        
        urllib.urlretrieve(i, '%s.jpg'%x)
        x+=1
    
    
    
url="http://tieba.baidu.com/p/2460150866"

html=getHtml(url)
getIMG(html)


    
    
    
    
    


    