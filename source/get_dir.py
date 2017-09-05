#! /usr/bin/env python
#coding=utf-8

import glob
import os

def get_dir(f):
    a=[]
    for i in glob.glob(f+"\*"):
        if os.path.isdir(i):
            a.append(i)
    if a:
        print a
    else:
        print "notdir"
        
        
get_dir('d:\source')
    
    