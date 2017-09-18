
class Foo():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print "%s-%s"%(self.name, self.age)

    def __call__(self):
        print "calling!"
    
    def __getitem__(self,key):
        print key + 10
    def __setitem__(self,key,value):
        print key, value
    def __delitem__(self,key):
        print "running delete it."
    def __len__(self):
        #print len(self)
        print "only a map????????????????"
        print len(self.name)
        print type(self.name)  #str  
        print self.name + "111111111"
 
    def __str__(self):
        return self.name  ###########need a attention

    
f1 = Foo("tom",21)
f1.show()
f1()

print "----------"
f1.__len__()
# print f1.__str__()
print f1

"""
after def __str__,  print f1  =  f1.__st__()
"""


f1[10]

f1["key1"]="value1"
f1["key1"]="value1"

del f1["key1"]
print f1.__dict__
"""
    print f1.__dict__()
TypeError: 'dict' object is not callable"""
# Just mapping style, haha  good name

print hasattr(f1,"name")
print getattr(f1,"name")
setattr(f1,"name","tom1")
setattr(f1,"newname","newtom")
print getattr(f1,"name")
print getattr(f1,"newname")

delattr(f1,"name")
print hasattr(f1,"name")

#instance, class, module are all object!!!!!!!!!!!!!!!!!!!!

import h003a

"""
import h003a.py
ImportError: No module named py
"""
# print hasattr(h003a,"f1")
# while True:
#     inp = raw_input(">>:")
#     # print inp
#     # print type(inp)
#     # print "inp"

#     if hasattr(h003a,inp):  # $$$$$can't use "inp", "inp" is just a new str
#         print "get it"
#         a=getattr(h003a,inp)  # $$$$$can't use "inp"
#         a()



print "nnnnnnnnnnneeeeeeeeeeeeewwwwwwwwwwwww"
class F():
    def __init__(self, key, value):
        self.dict = {}
        self.dict[key] = value

    def __getitem__(self,key):
        print self.dict[key]

    def __setitem__(self,key,value):
        self.dict[key] = value

ff = F("name","tom")
ff["name"]
ff["age"]=21
ff["age"]



