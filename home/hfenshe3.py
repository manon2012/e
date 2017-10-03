class Foo():
    code = 86
    def __init__(self,name,age):
        self.name = name
        self.age =age
    def eat (self):
        print "china like eat"

def out(self):
    print "it's out method"

f1 = Foo("tom",21)

choice =raw_input(">>")  
setattr(f1,choice,out) # can loaded function outside of a class
fun=getattr(f1,choice)
fun(f1)




print hasattr(f1,"eat")
print hasattr(f1,"name")
print hasattr(f1,"code")


print getattr(f1,"eat")
print getattr(f1,"eat")()
print getattr(f1,"name")
print getattr(f1,"code")

print "set____________"
setattr(f1,"name","newtom")
setattr(f1,"code","new86")
setattr(f1,"eat"," n")

print getattr(f1,"eat") #n
#print getattr(f1,"eat")()  #TypeError: 'str' object is not callable

print getattr(f1,"name")
print getattr(f1,"code")


delattr(f1,"name")
print hasattr(f1,"name")


print "classs---------"
print hasattr(Foo,"name")  #false
print hasattr(Foo,"code")
print hasattr(Foo,"eat")

setattr(Foo,"name","111")
setattr(Foo,"code","111")
setattr(Foo,"eat","111")

print getattr(Foo,"name")
print getattr(Foo,"code")
print getattr(Foo,"eat")



print "from fanshe2"
import hfanshe2
print hasattr(hfanshe2,"name")
print hasattr(hfanshe2,"FromS2")



