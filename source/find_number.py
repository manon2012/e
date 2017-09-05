#! /usr/bin/env python
#coding=utf-8

#def find_number(a):
#    
#    b=[]
#    for i in a:
#        try:
#            int(i)
#            b.append(i)
#        except Exception,e:
#            print e
#    print b
#    print str(b)
#    


def get_fresh(a):
    aa=a.upper()
    print aa
    b=[]
    
    for i in aa:
        if i not in b:
            b.append(i)
    print (''.join(b))


    
#    def getUniqueItems(iterable):
#    result = []
#    for item in iterable:
#        if item not in result:
#            result.append(item)
#    return result
#    
#    print (''.join(getUniqueItems(list('apple'))))
#    
      
  
  
def  get_dict(a):
    aa=a.upper()
    d={}
    for i in aa:
        d[i]=aa.count(i)
        
    print d    
    
     
    
a = "aAsmr3idd4bgs7Dlsf9eAF"
get_fresh(a)

get_dict(a)