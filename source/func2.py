#! /usr/bin/env python
#coding=utf-8

def func2(*nums):
    
    a=[]
    for i in nums:
        if not isinstance(i, str):
            return "parameter error"
        a.append(i)
        
    print max(a, key=len)  
    
    
func2("hi","china")    