
class Rec():
    def __init__(self):
        self.w=0
        self.h=0
        #self.size = 0
        
    def getSize(self):
        return self.w,self.h
    
    def setSize(self,size):
        self.w,self.h = size
    
    # def property(self,getSize,setSize):   not work in this
    #     return self.getSize, self.setSize
    size = property(getSize,setSize)
        
r = Rec()
r.w = 0
r.h = 0

print r.getSize()

r.setSize((10,1000))
"""    r.setSize(10,1000)
TypeError: setSize() takes exactly 2 arguments (3 given)"""
print r.getSize()

r.size=1000,2000

"""    r.size(1000,2000)
TypeError: 'tuple' object is not callable"""
print r.h,r.w     #1000  10



r2 = Rec()
r2.h = 21
r2.w = 21

print r2.size   #goes to getSzie
r2.size =200,200  # NOOOOOOOOT goes to setSize?????????????????????????
print r2.size
print r2.h, r2.w