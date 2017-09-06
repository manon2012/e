def showprime2(x):
    lista = []
    for i in range(1,x):
        for ii in range(2,i):
            if i%ii ==0:
                pass
            else:
                lista.append(i)
                break
                
    print lista
showprime2(21)

