#! /usr/bin/env python
#coding=utf-8


def f1(a,b,c):
    
    a.extend(b)
    a.extend(c)
    print a
    print type(a)
    print max(a)


f1([1,2,3],[1,5,65],[33,445,22])




def f2(a,b,c):
    
    a.extend(b)
    a.extend(c)
    print a
    print type(a)
    print max(a)
    
f2(a=[1,2,3],c=[1,5,65],b=[33,445,22])


print "----------------"



def f3(*kargs):
    a=[]
    for i in kargs:
        a.extend(i)
    print max(a)
 
    
f3([1,2,3],[1,5,65],[33,445,22])


print "$$$----------------"

def f4(**kwargs):
    a=[]
    for i in kwargs:
        #print kwargs.value(i)
        a.extend(kwargs[i])  #kwargs(i)  TypeError: 'dict' object is not callable
    print max(a)
        
        
f4(a=[1,2,3],b=[1,5,65],c=[33,445,22])
    
    
    
    
    
    
def fun4(**kwargs):
    print kwargs.values()
    b=[]
    for key in kwargs:
        b.extend(kwargs[key])
    print "b:",b
    print max(b)

fun4(a=[1,2,3],b=[1,5,65],c=[33,445,22])


def testkr(*kargs):
    return kargs


print testkr(12,"st",[123])
    
    
def testkrr(**kwargs):
    return kwargs

print testkrr(a=1,b=2,c=3)
