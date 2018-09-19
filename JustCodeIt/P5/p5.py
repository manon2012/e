
a=100
b=10
print  abs(a)

print divmod(a,b)
print coerce(a,b)

print pow(2,3)
print 2**3

print ord('A')
print chr(97)



#print dir(random)

import random

alist=[]
for i in range(10):
    a = random.randint(0, 10)
    alist.append(a)
print alist

def code():
    aa=''
    for i in range(6):
        a= random.choice(range(10))
        aa+=str(a)
    return  aa

print code()

import string

listb=[]
for w in string.lowercase[:]:
    listb.append(w)
print listb


a=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
newcode=''
for i in range(4):

    if i%2==0:
        newcode += str(random.choice(a))
    else:
        newcode += str(random.choice(b))
print newcode



newlist=[222,222,222]
a.extend(newlist)
print a

a.append(newlist)
print a


abc= 'abc'
print list(abc)
print str(a)
print tuple(abc)


for index, value in enumerate(abc):
    print index ,":",value

#lista=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print max(([9,9],[1,2,3],[1,2,3,4]),key=len)



r1=range(10)
print r1
print list(reversed(r1))

#print sum(r1,1000)

def f(x,y):
    return  x+y

try:
    aa=reduce(f,[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
except Exception as e:
    print e
print aa


a1=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a2=sorted(a1,reverse=True)


print zip([1,2,3,4,5,6],['a','b','c'])



a2.sort()
print a2


# str1 = 'abcdsdfjiopwerfdjsaapple'
# print str1.index('apple'), str1.find('abc')
# print str1.find('z')
# print str1.index('z')
#
# print  "abc".index('z')
#
#
#
# str0 = "this is string example....wow!!!";
# str2 = "exam";
#
# print str0.index(str2)
# print str0.index(str2, 10)
# print str0.index(str2, 40)



for i in range(10):
    print i
    if i >6:
        break
else:
    print 'just test for else'


s1='hello'
s2='pycharm'
import time
c1=time.time()
for i in range(100):
    s3=''.join([s1,str(i)])
print s3
c2=time.time()
print c2-c1


c3=time.time()
for i in range(100):
    s4 = s1 + str(i)
print s3
c4=time.time()
print c4-c3


