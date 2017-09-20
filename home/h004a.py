def gen():
    print "ok1"
    yield 1
    
    print "ok2"
    yield 2
    
# g=gen()
# r1=g.next()
# print r1
# 
# r2=g.next()
# print r2



def gen2():
    print "ok1"
    count = yield 1
    print count
    
    print "ok2"
    yield 2
    
g2=gen2()
g2r1=g2.send(None)
print g2r1

g2r2=g2.send("new")
print g2r2




def gen3(value):
    while True:
        new = (yield value)
        if new is not  None:
            value =new
g3=gen3(42)
print g3.next()
print g3.send("hi")


    