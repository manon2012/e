

def func(i):
    return str(i)

aa=[1,2,3,4,5,6]

print map(func,aa)


def funca(i):
    return i+10

print filter(funca,aa)   #filer not change anything, just filter


def funcb(i,j):
    return i+j

print reduce(funcb,aa)


lambda x,y :x+y


import keyword
print keyword.kwlist
