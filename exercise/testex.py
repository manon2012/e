#! /usr/bin/env python
#coding=utf-8


def TestEx():
    try:
        x=int(raw_input("first one:"))
        y=int(raw_input("second one:"))
        #z=(int)x/(int)y 
        z=x/y
        
#   except Exception,e:
#        print e
       
    except(ZeroDivisionError,TypeError),e:
         print e
        
    else:
        print z  
    finally:
        print "haha"
    
TestEx()