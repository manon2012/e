#! /usr/bin/env python
#coding=utf-8


def ss(d1):
    
    if d1==1:
        print "1 is not"
    elif d1==2:
        print "2 is not"
    
    else:
        
    
        for i in range(2,d1):
            if d1%i==0:
                return False
            #print "%s it is"%d1
        return True
            
    
#print ss(17)
#print ss(18)
#print ss(19)
#print ss(77)
#ss(100)
#ss(101)
#ss(17)
#ss(1)
#ss(2)

pri100=[]
for ii in range(100):
    if ss(ii):
        pri100.append(ii)
    
print pri100



#just more that 10000

for i in range(10000,20000):
#    if ss(i):
#        print i
#        break
    
#     if ss(i):
#        #print i
#        aa.append(i)
#        #print aa
#        if len(aa)==3:
#            break
     aa=[]     
     while(len(aa)<4):
        if ss(i):
            aa.append(i)
            continue
print aa

