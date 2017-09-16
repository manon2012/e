
nest =[[1,2],['a'],[3,4,5]]

def flatten(nest):
    for sublist in nest:
        for element in sublist:
            yield element

print type(flatten) #<type 'function'>
print type(flatten(nest)) #<type 'generator'>

for i in flatten(nest):
    print i


print [x for x in range(10)]

def fx(x):
    return x*x
print [fx(x) for x in range(10)]



print (x for x in range(10))  #<generator object <genexpr> at 0x0175C7B0>
for ii in (x for x in range(10)):
    print ii
def f():
    print "ok1"
    yield 11
    #b=yield 11
    """
     b=yield 11
     a.next()
    print b
    Traceback (most recent call last):
  File "h004.py", line 41, in <module>
    print b
NameError: name 'b' is not defined,,,,,,,,,,,b is out side of function
    """

    print "ok2"
    yield 22

print "11111111111"
for i in f():
    print i

print "22222222222"
a = f()
b=a.next()
print b

c=a.next()
print c



print "Test Send"
def TestSend():
    print "T1"
    a=yield 1
    print a

    print "T2"
    b=yield 2

# TestSend().send(None)
# TestSend().send("aa")
# print a

t = TestSend()
r1=t.send(None)
print a  #<generator object f at 0x0174A940>

r2=t.send(2017)
print r1,r2




"""
TestSend.send(None)  nono, the genarator's method


TestSend().send(None)
TestSend().send("aa")

 T1
Traceback (most recent call last):
  File "h004.py", line 67, in <module>
    TestSend().send("aa")
TypeError: can't send non-None value to a just-started generator

"""

