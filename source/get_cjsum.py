#! /usr/bin/env python
#coding=utf-8

def get_cjsum():
    a=0
    total_list=[x*x for x in range(101)]
    print total_list
    for i  in total_list:
        a+=i
    print a
        
        
        
get_cjsum()