#! /usr/bin/env python
#coding=utf-8

def get_num(num):
    b=[]
    for i in num:
        #b=[] error
        if not isinstance(i,int):
           print "%s not number"%i
        else:
            b.append(i)
    
    print [x for x in b if x%2==0]
    
    
    
get_num([1,2,3,4,5,6,7,8,9,10,"aaa"])