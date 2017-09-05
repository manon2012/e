
def fun1(*num):
    tl=[]
    for i in num:
        if not isinstance(i,int):
            print "%s should be int"%i
            break
        tl.append(i)
    if tl:
        print max(tl)
    else:
        pass
    
#fun1(1,2,3)
fun1("1",2,3)
    
    
    
def fun2(*num):
    tl=[]
    for i in num:
        if isinstance(i,str):
            tl.append(i)
        else:
            pass
    print max(tl,key=len)
    
fun2("i","love","elala")
fun2("i","love",2017)

            
            
