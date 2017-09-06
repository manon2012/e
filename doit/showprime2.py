def showprime2(x):
    lista = []
    for i in range(2,x):
        for ii in range(2,i):
            if i%ii ==0:
                break
        else:
            lista.append(i)

                
    print lista
showprime2(21)

