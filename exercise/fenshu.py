#! /usr/bin/env python
#coding=utf-8


with open("fenshu.txt") as f:
    f1=f.readlines()
    print f1
    
for user in f1:
    #print user
    f2=user.split()
    print f2
    sum=0
    for i in f2[1:]:
        sum +=int(i)
    print f2[0],sum
    newf=open("fenshudone2.txt","a")
    print >>newf, f2[0],sum
        
        
    
    
#    open("fenshudone.txt")
#    print >>"fenshudone.txt", user,sum
#    AttributeError: 'str' object has no attribute 'write'

'''

1
down vote
accepted
The code you posted doesn't cause the error you say it does.

Regardless, the error is telling you exactly what the problem is: you're referencing the "write" method on a string. Maybe you think you're referencing it via an open file object but you are actually referencing it on a string.

Without seeing your code we can't debug it any further, but it's highly likely you're reusing a variable to be both a filename and an open file.

'''

       
    
    
    