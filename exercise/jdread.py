#! /usr/bin/env python
#coding=utf-8

import re
import urllib2

with open("jdread.txt","r") as f:
    ff=f.read()
    #print ff
    


def getJD(ff):
    #reg = r'title="()" '
    #reg = r'href="(.+?\.html)" '   ok
    #reg = r'title="(.+?)" '  $not readable char
    
    
    #reg = r'src="(.+?\.jpg)" pic_ext'
    reg = r'src="(.+?\.jpg)"'  
    #print type(reg)
    
    regall=[r'src="(.+?\.png)"', r'href="(.+?\.html)" onclick'  ]
    #regall=[r'data-price="(.+)"' ]
    #print regall
    
    result={}
    for r in regall:
       jdreg = re.compile(r)
       jdlist=re.findall(jdreg,ff)
       #result.append(jdlist)
       print jdlist
#       item=["jpg","url"]
#       for i in item:
#           result[i]=jdlist
#           break
    
    
    print result
        
        
getJD(ff)