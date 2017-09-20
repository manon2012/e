__metaclass__ = type

def showpage():
    
    while True:
        inp = int(raw_input(">>"))
        print (inp-1)*10+1,"-",inp*10
    
    
#showpage()


class Foo():
    def __init__(self,name):
        self.name = name
        
    def f(self):
        print  "f"
     
    @property    
    def fa(self):
        print  "fa"
    
    @fa.setter
    def fa(self,value):
        print value
        
    @fa.deleter
    def fa(self):
        print "66"

    def fb(self):
        print  "fb"  

f1 = Foo("tom")
print  f1.name
f1.f()
f1.fa
"""#f1.fb #nothing output, why not throw exception?????????????????????
Need add __metaclass__ = type
"""

f1.fa =123

del f1.fa







###From web
#!/usr/bin/env python  
# -*- coding: utf-8 -*-  
# blog.ithomer.net  

Print "way I"
class Cls(object):  
    def __init__(self):  
        self.__x = None  
      
    def getx(self):  
        return self.__x  
      
    def setx(self, value):  
        self.__x = value  
          
    def delx(self):  
        del self.__x  
          
    x = property(getx, setx, delx, 'set x property')  
  
if __name__ == '__main__':  
    c = Cls()  
    c.x = 100  
    y = c.x  
    print("set & get y: %d" % y)  
      
    del c.x  
    print("del c.x & y: %d" % y)     




Print "way II"
class Cls(object):  
    def __init__(self):  
        self.__x = None  
         
    @property  
    def x(self):  
        return self.__x  
     
    @x.setter  
    def x(self, value):  
        self.__x = value  
         
    @x.deleter  
    def x(self):  
        del self.__x  
  
if __name__ == '__main__':  
    c = Cls()  
    c.x = 100  
    y = c.x  
    print("set & get y: %d" % y)  
      
    del c.x  
    print("del c.x & y: %d" % y)   
