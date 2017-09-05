#! /usr/bin/env python
#coding=utf-8


def get_fundoc(func):
    if func.iscallable:
        print func.__doc__
    
    
    
get_fundoc(list)
    