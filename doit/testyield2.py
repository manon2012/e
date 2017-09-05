

nest2=[['a'], ['ab',['ab']], ['abc',[['a'], ['ab']]]]


def testyield2(nest2):
    try:
        for subnest in nest2:
            for element in testyield2(subnest):
                yield element
    except TypeError:
        yield nest2
    
for ii in testyield2(nest2):
     print ii
#list(testyield2(nest2))


def flatten(nested):  
    try:  
        for sublist in nested:  
            for element in flatten(sublist):  
                yield element  
    except TypeError:  
        yield nested  