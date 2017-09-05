#! /usr/bin/env python
#coding=utf-8

def get_funcname(func):
    
    if callable(func):
        print func
    else:
        print "func %s not callable"%func
    
a=[]    
    
get_funcname(dir)
get_funcname(a)