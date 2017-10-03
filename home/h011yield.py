
def test_yield():
    print "ok1"
    y1=yield 1
    print y1


    print "ok2"
    y2=yield 2
    print y2


# for i in test_yield():
#     print i




# a1=test_yield().next()
# print a1
# a2=test_yield().next()
# print a2
# ok1
# 1
# ok1
# 1

# a=test_yield()
# a1=a.next()
# print a1
# a2=a.next()
# print a2

b=test_yield()
b1=b.send(None)
print b1

b2=b.send("new")
print b2