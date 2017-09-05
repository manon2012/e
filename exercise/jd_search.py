#! /usr/bin/env python
#coding=utf-8

"""
url: "http://search.jd.com/Search?keyword=%E5%B9%BC%E7%8C%AB%E7%8C%AB%E7%B2%AE&enc=utf-8#filter"


print jd_search(keyword)

[dict,dict,dict]
dict {pic:'',title:'',price:'',url:''}

"""

import re
import urllib


def getHtml(url):
    f=urllib.urlopen(url)
    html=f.read()
    return html


url="http://search.jd.com/Search?keyword=%E5%B9%BC%E7%8C%AB%E7%8C%AB%E7%B2%AE&enc=utf-8#filter"


html=getHtml(url)
with open("jd.txt","w") as g:
    g.write(html)




def jd_search(keyword):
    pass


a=[("url","jd.com"),("price",100),("img","jd.com\1.jpg")]
b=[("url","jd.com"),("price",200),("img","jd.com\1.jpg")]



#print dict(a)

#c=[a,b]

#[dict,dict]

c=[[('url', 'jd.com'), ('price', 100), ('img', 'jd.com\x01.jpg')], [('url', 'jd.com'), ('price', 200), ('img', 'jd.com\x01.jpg')]]

for i in c:
    print dict(i)




