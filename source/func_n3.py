#! /usr/bin/env python
#coding=utf-8

import urllib
import re

def func_n3(url):
    a=urllib.urlopen(url)
    b=a.read()
    #print b
    print type(b)
    
    
    c=open(r'd:\source\net\link.txt','w')
    c.write(b)
    
    
    number=re.search(r'http://(.*?)', b)
    print type(number)
    print number
    
    
    print b.count("http")+b.count("https")
   
    
 
    

func_n3("http://www.so.com")


