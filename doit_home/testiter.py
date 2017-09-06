a = ["a", "ab", "abc"]

b = iter(a)

print b

print b.next()
print b.next()
print b.next()

print '$$$'
nest = [['a'], ['ab'], ['abc']]


def testyield(nest):
    for subnest in nest:
        for element in subnest:
            yield element


for i in testyield(nest):
    print i




nest2=[['a'], ['ab',['ab']], ['abc',[['a'], ['ab']]]]


def testyield2(nest2):
    '''doc here'''
    try:
        for subnest in nest2:
            for element in testyield2(subnest):
                yield element
    except TypeError:
        yield nest2
    
for ii in testyield2(nest2):
    print ii



