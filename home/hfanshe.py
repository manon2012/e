
import hfanshe2


hfanshe2.FromS2()
print hfanshe2.name

print hasattr(hfanshe2,"name")
inp = raw_input(">>")
if hasattr(hfanshe2,inp):
    r1= getattr(hfanshe2, inp)

else:
    print 404

class Foo:
    def __init__(self, name):
        self.name = name
        self.n = 2018

f1 = Foo("py")

t1= hasattr(f1, "name")
print t1

t2=getattr(f1,"n")
print t2

setattr(f1,"n","2018new")

t3=getattr(f1,"n")
print t3

delattr(f1,"n")
t4= hasattr(f1, "n")
print t4

