
class dog:
    name = 'JD'
    def __init__(self,color):
        self.color = color

    def eat(self,times):
        print dog.name

        for i in range(times):
            print "%s eat..."  % self.color

d1 = dog("red")
d1.eat(3)


#import p1


import sys
print dir(sys)

sys.stdout.write('showinconsole')
print sys.platform
print sys.version
#print help(sys)

aa=range(1,10,2)

#a= raw_input("-->")
#print type(a)

print sum(aa,1)
print  list.__doc__

aa.append(100)
print aa

#sys.exit()  exit python interpreter

import os
print os.linesep
print "1"

s1= "$$12399990000$$"
print s1.strip("@")


a,b,c=1,2,'3'
print a,b,c
print type(a )
print type(b )
print type(c )
a,b=b,a
print a,b

import keyword
print keyword.iskeyword(list)