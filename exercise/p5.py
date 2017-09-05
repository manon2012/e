
#coding=utf-8

"""
1 用lambda和filter完成下面功能：输出一个列表，列表里面包括：1-100内的所有偶数。（提示：可以用filter,lambda）

2 用位置匹配，关键字匹配，收集匹配(元组收集,字典收集)分别写4个函数，完成功能；

传递3个列表参数：

[1,2,3],[1,5,65],[33,445,22]

返回这3个列表中元素最大的那个，结果是：445


3 递归函数解释，用自己的话说明这个递归函数的工作流程。

def func1(i):
	if i<100:
		return i + func1(i+1)
	return i
print func1(0)

"""


#print filter(lambda x: x%2==0, range(100))


def f1(a,b,c):
    tl=[]
    tl=a+b+c
    #print type(tl)
    print  max(tl)

#f1([1,2,3],[1,5,65],[33,445,22])


def f2(a=[],b=[],c=[]):
    d=[]
    d=a+b+c
    print max(c)
    
#f2(a=[1,2,3],b=[1,5,65],c=[33,445,22])


def f3(*num):
    tl=[]
    for i in num:
        tl.extend(i)
    print max(tl)

#f3([1,2,3],[1,5,65],[33,445,22])


def f4(**num):
    tl=[]
    for i in num.values():
        tl.extend(i)
    print max(tl)
        
#f4(a=[1,2,3],b=[1,5,65],c=[33,445,22])



def func1(i):
    if i<100:
        return i + func1(i+1)
    return i
print func1(0)
print func1(1000)

