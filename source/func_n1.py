#! /usr/bin/env python
#coding=utf-8

import urllib

import uuid
import os


def func_n1(url, folder_path):
    
    a=urllib.urlopen(url)
    
    b=a.read()
    
    print b
    
    
    #c=open(r'd:\source\net\1.txt','w')
    
    filename = str(uuid.uuid4())
    
    print filename
    print folder_path
    #print folder_path+filename   //  d:\source\net30b62b75-135c-4ce2-b2f7-24e72835d066
    
    
    c=open(os.path.join(folder_path,filename),'w')
    c.write(b)
    
    
url="http://www.ca.com"
func_n1(url,r"d:\source\net")