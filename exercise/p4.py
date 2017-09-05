# coding:utf-8

#1 定义一个方法get_fundoc(func),func参数为任意一个函数对象，返回该函数对象的描述文档，如果该函数没有描述文档，则返回"not found"


def get_fundoc(func):
    if not callable(func):
        print "func is not callable"
        
    elif type(func)== "<type 'classobj'>":
        print "it's a ..."
        
        
    else:
        print func.__doc__
        

class a:
    pass
    
get_fundoc(dir)
get_fundoc(a)



def get_cjsum(x):
    sum=0
    for i in range(x+1):
        sum+=i*i
    print sum
    
get_cjsum(100)



def list_info(alist):
#    alist=[1,2,2]
#    print "newlist:", alist
     newa=alist[:]
     newa[0]=100
     print newa
    
alist=[1,2,1]

list_info(alist)

print alist






"""
# coding:utf-8

#1 定义一个方法get_fundoc(func),func参数为任意一个函数对象，返回该函数对象的描述文档，如果该函数没有描述文档，则返回"not found"

def get_fundoc(func):
    #使用callable判断是否能被调用
    if not callable(func):
        return 'the func not function'
    elif str(type(func)) == "<type 'classobj'>" or str(type(func)) == "<type 'module'>":
        return 'this not a function'
    else:
        if func.__doc__ == None:
            print 'not doc'
        else:
            print func.__doc__
#get_fundoc(max)


#2 定义一个方法get_cjsum(),求1-100范围内的所有整数的平方和。返回结果为整数类型。

def get_cjsum():
    count = 0
    for i in range(1,101):
        count+=i*i
    print count
#get_cjsum()

3 定义一个方法list_info(list), 参数list为列表对象，怎么保证在函数里对列表list进行一些相关的操作，不会影响到原来列表的元素值，比如：

a = [1,2,3]

def list_info(list):
   '''要对list进行相关操作，不能直接只写一句return[1,2,5]，这样就没意义了'''

print list_info(a):返回结果：[1,2,5]

print a 输出结果：[1,2,3]

写出函数体内的操作代码。
#这里使用列表的分片将l的值重新赋值给a，这里a就是一个新的列表对象，而不是l列表的另一个映射。
def list_info(l):
    a = l[:]
    a[0] = 'test123'
    print a

#c = [3,1,2,4]
#list_info(c)
#print c

#4 定义一个方法get_funcname(func),func参数为任意一个函数对象，需要判断函数是否可以调用，如果可以调用则返回该函数名(类型为str)，否则返回 “fun is not function"。
    
def get_funcname(func):
    if callable(func):
        if 'func_name' in dir(func):
            print func.func_name
        elif str(type(func)) == "<type 'classobj'>" or str(type(func)) == "<type 'module'>":
            print 'this not a function'
        else:
            print 'the func is builtin_function_or_method!'
    else:
        'fun is not function'

#get_funcname(abc)
    


"""