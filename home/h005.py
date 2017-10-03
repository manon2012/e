

alist = [1,2,3,4,5,6]

a= iter(alist)   #alist.__iter__()
print list(a)


for i in a:
    print i
"""
1. iter()
2. .next()
3. stopIteration
"""
