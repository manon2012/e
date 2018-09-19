#
#
# while True:
#
#     try:
#         # a='a'
#         # a=int(a)
#         a = int(raw_input("please input a, q to quit--->"))
#         if a==666:
#             break
#         #raise  TypeError
#
#     except ValueError :
#         print "got ValueError, continue..."
#         continue
#     except Exception as e:
#         print "got Exception, continue..."
#         print e
#         continue
#
#     if a>0 and a<5:
#         print "normal"
#         continue
#     elif a >=5 and a <10:
#         print "good"
#         continue
#     elif a==10:
#         print "excellent"
#         continue
#
#



print range(10)
lista= [1,2,3]

print range(len(lista))

for x,y in enumerate(lista):
    print x,":",y


class Person:
    def eat(self):
        print "eat"

p1 = Person()
p1.eat()
Person.eat(p1)

print p1.eat
print Person.eat


print [x for x in range(10) if x%2==0]



handle = open('p1.txt','r')
print handle.read()


def f1(num):
    num=num*2

print f1(1)