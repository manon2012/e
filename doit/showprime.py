
def showprime(x):
    lista=[]
    for i in range(2,x):
        for ii in range(2,i):
            if i%ii==0:
                break
        else:
            lista.append(i)
    return lista

listb=showprime(100)
print len(listb)