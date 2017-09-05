#! /usr/bin/env python
#coding=utf-8
import random

def addcode():
    a=random.sample(['a','b','c','d','e','f','g','g','i','j'],6)
    b=''.join(a)
    return b


alist=[]
x=int(raw_input("duoshaoge:"))

for i in range(x):
#    print i
    new=addcode()
    #newlist=alist.extend(new)
    alist.append(new)
print alist
    

    



