#! /usr/bin/env python
#coding=utf-8

def test_exception():
 
#    try:
#       aa=open (r'd:\source\2.txt','w')
#    
#       try:
#           aa.write("babld123")
#       finally:
#           print "write done"
#           aa.close
#    
#    
#    except IOError:
#        print "file not found"
  
        
    try:
        a=1/2
    except Exception,e:
        print e
    else:
        print "succesful, %s"%a


test_exception()