#! /usr/bin/env python
#coding=utf-8


    
import glob
def func5(d):
    for i in glob.glob(d+'\*'):
        print i
    
print func5("d:\source")
