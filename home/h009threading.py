
#-*- coding:utf-8 *-*
import threading,time

def run(n):
    print "%s is running 哈哈"%n  #这里的sleep 才能看出效果

# run("tom")
# run(100)

# t1=threading.Thread(target=run, args=("t1",))
# t2=threading.Thread(target=run, args=("t2",))

# t1.start()
# t2.start()
t1= time.time()
alist=[]
for i in range(10):
    i=threading.Thread(target=run, args=(i,))
    #i.start()
    alist.append(i)
    #time.sleep(0.1)
#time.sleep(3)
for i in alist:
    i.start()


print time.time()-t1



# class MyClass(threading.Thread):
#     def __init__(self,n):
#         super(MyClass,self).__init__()
#         self.n=n
#     def run(self):
#         print "this is my run %s"%self.n

# c1=MyClass("t1")
# c1.start()

    