alist = [1000,6,2,5,3,60]

for i in range(len(alist)):
    for j in range(len(alist))[i+1:]:
        if alist[i]  > alist[j]:
            tmp= alist[i]
            alist[i] = alist[j]
            alist[j] =tmp

print  alist