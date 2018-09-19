
import p3test

print __name__
nn=__name__
print nn

import profile


print type(type(1))


a="abc"
b="ab"
print cmp(a, "abc")
lista=[1,2,3]
print str(lista)

import sys
#print help(sys)

class teststr:
    def __init__(self,name):
        self.name = name
    # def __str__(self):
    #     return self.name

t1=teststr('namewitht1')
t2=teststr('namewitht2')

print t1


print isinstance(t1,teststr)
print isinstance(lista,tuple)


from types import ListType,IntType
import time

c1=time.time()
i=0
while True:

    if type(lista) is ListType:
    #if type(lista)== ListType:
        i+=1
    if i>10:
        break
c2=time.time()
print c2-c1


import  operator
print dir(operator)

