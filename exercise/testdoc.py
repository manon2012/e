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


#s="����"?
#
#if isinstance(s, unicode):?
##s=u"����"?
#print s.encode('gb2312')?
#else:?
##s="����"?
#print s.decode('utf-8').encode('gb2312')






#def outer(func):                    # ����һ��outer������Ϊװ����
#    def inner():���������������������� # ���ִ��inner()�����Ļ��������£�
#        print('start')              # 1�����ȴ�ӡ���ַ���start����
#        r=func()                    # 2��ִ��func������func�����൱��def f(): print('��') 
#        print('end')                # 3�����ź�����ӡ��end��
#        return r                    # 4����func�����Ľ������
#    return inner
#   
#@outer
#def f():              # f=outer(f)=innner
#    print('��')
#   
#f()                   # f()�൱��inner(),ִ��inner�����Ĳ��迴���涨�崦��ע��<BR>#��ӡ���˳��Ϊ   start �� end
#







