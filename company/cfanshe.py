import cfanshe2

cfanshe2.f1()

print hasattr(cfanshe2,"f1")

ff1= getattr(cfanshe2,"f1")
ff1()



class foo:
    def __init__(self,name):
        self.country = "china"
        self.name = name
        self.n = 2017
    
    def git(self):
        print "git"


f1 = foo("tom")

# while True:
#     inp =raw_input(">>")
#     if hasattr(f1,inp):
#         print "y"
#         f1a=getattr(f1,inp)
#         print f1a

print getattr(f1,"n")


'''
This is the counterpart of getattr().
 The arguments are an object, a string and an arbitrary value.
  The string may name an existing attribute or a new attribute. 
  The function assigns the value to the attribute, provided the object allows it.
   For example, setattr(x, 'foobar', 123) is equivalent to x.foobar = 123.
'''
try:
    setattr(f1,"n1",2018)
except Exception,e:
    print "don't have"
else:
    print "done"
finally:
    print "$$$$$$$"
    print f1.n1 
    print "$$$$$$$"

print getattr(f1,"n")
# try :
    

# expect Exception, e:
#     print "wrong"

# else:
    
try:
    delattr(f1,"n")
    print getattr(f1,"n")
except AttributeError,e:
    print "not found"
else:
    pass
finally:
    pass
