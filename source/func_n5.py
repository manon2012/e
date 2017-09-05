#! /usr/bin/env python
#coding=utf-8

import os
import glob
def func_n5(folder):
    
    for item in glob.glob(folder+'\*'):
        print item
        if not os.path.isdir(item):
             os.remove(item)
        else:
             func_n5(item)
             os.rmdir(item)
                
        
        
func_n5(r'd:\source\net')