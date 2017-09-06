
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


