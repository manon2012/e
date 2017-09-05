
def showprime(x):
    lista=[]
    for i in range(1,x):
        for ii in range(1,i):
            if i%ii==0:
                pass
            else:
                lista.append(i)
    print lista

showprime(10)