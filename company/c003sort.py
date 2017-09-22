#encoding =utf-8
alist = [1000,6,2,5,3,60]


def bubble_sort(args):
    for i in range(len(alist)):
        for j in range(len(alist))[i+1:]:
            if alist[i]  > alist[j]:
                tmp= alist[i]
                alist[i] = alist[j]
                alist[j] =tmp

    print  alist

bubble_sort(alist)



# alist = [6,2,5,3,60]
# def insert_sort(args):
#     for i in range()
a= [6,2,5,3,60]
for j in range(1, len(a)):
    key = a[j]
    i = j - 1
    while i >= 0 and a[i] > key:
        a[i + 1] = a[i]
        i = i - 1
    a[i + 1] = key
print a
