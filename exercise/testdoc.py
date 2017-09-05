#import time
#
#coding=utf-8
#
#def foo(name):
#    print "e%s"%name
#    
#
#def timeit(func):
#    def wrapper(*p):
#        t1=time.time()
#        func(*p)
#        t2=time.time()
#        print t2-t1
#    return wrapper
#
#    
##timeit(foo('e'))  TypeError: 'NoneType' object is not callable   
#
##method A
#foo=timeit(foo)
#foo('e')
#
#
#@timeit
#def foo2(name2):
#    print "%s"%name2
#foo2('lala')

#method B
#@timeit
#def foo(name):
#    print "e%s"%name
#foo('e')




#def connect_db():
#    print "connect"
#    
#def close_db():
#    print "colse"
#    
#def query_user():
#    connect_db()
#    print "query db"
#    close_db()
#
#query_user()


#s="中文"?
#
#if isinstance(s, unicode):?
##s=u"中文"?
#print s.encode('gb2312')?
#else:?
##s="中文"?
#print s.decode('utf-8').encode('gb2312')






#def outer(func):                    # 定义一个outer函数作为装饰器
#    def inner():　　　　　　　　　　　 # 如果执行inner()函数的话步骤如下：
#        print('start')              # 1、首先打印了字符‘start’，
#        r=func()                    # 2、执行func函数，func函数相当于def f(): print('中') 
#        print('end')                # 3、接着函数打印‘end’
#        return r                    # 4、将func函数的结果返回
#    return inner
#   
#@outer
#def f():              # f=outer(f)=innner
#    print('中')
#   
#f()                   # f()相当于inner(),执行inner函数的步骤看上面定义处的注释<BR>#打印结果顺序为   start 中 end
#







