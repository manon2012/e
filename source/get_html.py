#! /usr/bin/env python
#coding=utf-8
import urllib
import re

def get_html(url):
    page=urllib.urlopen(url)
    html=page.read()
    return html
    

def get_img(html):
    reg = r'src="(.+?\.jpg)"'
    imgre=re.compile(reg)
    imglist = re.findall(imgre,html)
     
    x=0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'%s.jpg' % x)
        x+=1
  
  
html = get_html("http://tieba.baidu.com/p/2460150866")
  
print get_img(html)
  




    



##coding=utf-8
#import urllib
#import re
#
#def getHtml(url):
#    page = urllib.urlopen(url)
#    html = page.read()
#    return html
#
#def getImg(html):
#    reg = r'src="(.+?\.jpg)" pic_ext'
#    imgre = re.compile(reg)
#    imglist = re.findall(imgre,html)
#    x = 0
#    for imgurl in imglist:
#        urllib.urlretrieve(imgurl,'%s.jpg' % x)
#        x+=1
#
#
#html = getHtml("http://tieba.baidu.com/p/2460150866")
#
#print getImg(html)
#