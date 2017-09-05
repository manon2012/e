#! /usr/bin/env python
#coding=utf-8
import glob
import os

def func_n2(folder_path):
    
    a=[]
    for i in glob.glob(folder_path+"\*"):
        #print i
        if not os.path.isdir(i):
            a.append(i)
    print a
    
    
    for i in a:
        b=open(i,'r')
        c=b.read()
        
        
        with open(r'd:\source\txt\01.txt','ab') as f:
                f.write(c)
        
#        d=open(r'd:\source\txt\all.txt', 'w')
#        d.write(c)
        
    
   
    


func_n2(r'd:\source\txt')