
import pdb

a=0
b=1

def fib(x):
    a,b=0,1
    #pdb.set_trace()
    while b<x:
        a,b=b,a+b
        yield b
        
for i in fib(10):
    print i    
    
#fib(10)


num=int(raw_input("how many do you want:"))

def fib2(num):
    tlist=[]
    a,b=0,1
    while b<num:
        a,b=b,a+b
        tlist.append(b)
    yield tlist
    
    
#fib2(10)
for i in fib2(num):
    print i
    
    