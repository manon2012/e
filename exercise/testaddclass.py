#! /usr/bin/env python
#coding=utf-8


class Testaddclass:
    num=0
    def __init__(self):
        Testaddclass.num+=1
        print Testaddclass.num
        
#        num+=1
#        print num
#        UnboundLocalError: local variable 'num' referenced before assignment
        
    
    def add(self):
        print "add"
        
        

t1=Testaddclass()
t1.add()

t2=Testaddclass()
t2.add()


class new(Testaddclass):
    def __init__(self):
        Testaddclass.num+=100
        print Testaddclass.num
        
        
    
       
    def newone(self):
        print "newone"
        
#    def add(self):
#        print "newadd"
        
n1=new()
n1.newone()
n1.add()