#! /usr/bin/env python
#coding=utf-8

import linecache

with open ("t.txt", 'r') as g:
    a=g.read().decode("utf-8-sig").encode("utf-8")
    print a
    
    
#f=linecache.getline("t.txt",1)
#print f

aa=linecache.getlines("t2.txt")
print aa

#
#fp = open("file.txt")
#data = fp.read().decode("utf-8-sig").encode("utf-8")






