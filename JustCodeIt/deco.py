import time

def wrapper(func):
    def inner(*args,**kwargs):
        print "before"
        c1 = time.time()
        ret = func(*args,**kwargs)
        time.sleep(1)
        c2 = time.time()
        print  c2-c1
    return  inner

#
# def f1():
#     c1= time.time()
#     time.sleep(1)
#     print "hi"
#     total = time.time() -c1
#     print total
@wrapper
def f1():
    print "f1 come"

f1()


