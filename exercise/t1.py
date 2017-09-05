
# 1-100 ou shu

import time

t=time.time()
#8.56
#print [x for x in range(100000) if x%2==0]


#6.35
#def getit(x):
#    for i in range(x):
#        if i%2==0:
#             yield i
#
#for i in getit(100000):
#    print i,
#
#
#print time.time()-t


import re
s = "[lol]please help to clear this markup[smile], thank you"

def clearit(s):
    r=r'\[.*?\]'
    print re.findall(r,s)

clearit(s)

'010-12345679'