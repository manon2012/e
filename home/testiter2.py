
newlist= [1,100,10000000000]

aa = iter(newlist)

print aa
print aa
print aa
print aa    
"""  it's just a address in memory
 <listiterator object at 0x0000000001DC3390>
<listiterator object at 0x0000000001DC3390>
<listiterator object at 0x0000000001DC3390>
<listiterator object at 0x0000000001DC3390>
"""

print aa.next()
print aa.next()
print aa.next()
#print aa.next()  
""" the fourth one will arise stopiteration exeption
Traceback (most recent call last):
  File "d:\git\e\doit\testiter2.py", line 20, in <module>
    print aa.next()
StopIteration
"""


alist = [[1,10],[100000000],[10000000]]

def nested(target):
    for subnest in target:
        for element in subnest:
            yield element

#nested(alist)
for i in nested(alist):
    print i

print "$$$$$$$$$$$$$$$$$$$$$"
blist = [[1,1],[10,[10,10]],[100,[100,[100]]]]

# def nestest(target):
#     for subnest in target:
#         try:
#             for element in nestest(subnest):
#                 print element
#         exception exception:  //exception color is correct
#                 print element
# nestest(blist)

def nestest(target):
    try:
        for subnest in target:
            for element in nestest(subnest):
                print element
    except TypeError:
        print subnest

nestest(blist)