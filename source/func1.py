#! /usr/bin/env python
#coding=utf-8

#def func1(lista):
#    print "big, small", max(lista),min(lista)
    

x=int(raw_input("please insert total number:"))
a=0
lista=[]
while a<x:
    y=int(raw_input("please insert %sth number:"%a))
    a+=1
    lista.append(y)    

print lista

print "big, small", max(lista),min(lista)




def num(*num):
#遍历参数列表，判断参数类型是否为整形
    for i in num:
        if not isinstance(i,int):
            return "参数错误,参数必须为整数"
    return max(num),min(num)

print num(2,3,6)

    


