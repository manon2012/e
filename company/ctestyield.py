

def f():
    print "ok1"
    count = yield 1
    print count

    print "ok2"
    yield 2


# f()
# print (type(f))   #print (type(f()))
# print (type(f()))  #print (type(f()))

a = f()
# a.next()
# a.next()
#a.next()

# for i in a:
#     print i

r1= a.send(None)
r2= a.send("e")

print r1,r2
