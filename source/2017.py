#! /usr/bin/env python
#coding=utf-8

def add(x,y):
    return x+y

a=add(1,2)


for x in range(100) :
    print x,


a= "\nthis is %s %s"%("my", "apple")
print a

b="this is {} {}".format("my","apple")
print b


c="this is {1} {0}".format("my","apple")
print c


d="this is {whose} {frute}".format(whose="my",frute="apple")
print d



aa=[("the %s" %d) for d in xrange(10)]
print aa






