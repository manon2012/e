
class TestNewObject(object):
    def __init__(self,name, phone):
        self.name = name 
        self.phone = phone
        print "create instance:", self.name
    
    def updatePhone(self,newphone):
        self.phone = newphone
        print "%s new phone is %s"%(self.name, self.phone)
        
        
a1= TestNewObject('tom',123)
print a1.name
print a1.phone
a1.updatePhone(321)


class NewClass(TestNewObject):
    def __init__(self,name, phone,id, email):
        #TestNewObject.__init__(self,name,phone)
        super(NewClass,self).__init__(name,phone)
        self.id=id
        self.email=email
        #self.name=name
        
        
        
    def updateemail(self,newemail):
        self.email=newemail
        print "new mail: %s"%(self.email)
        
a2= NewClass('jj',123,'id007','1@2.com')
a2.updatePhone(222)
#a2.updateemail('22@22.com')



class newone(object):
    
    def __init__(self):
        pass
    
    name="china"
    
    def eat(self):
        num=3
        print "eat %s"   % num
        self.__sleep()
        
    def __sleep(self):
        print "i sleep"
    
    @classmethod  
    def cc(self):
        print "classmethond"
    
    @staticmethod
    def ss():
        print "staticmothod"

tom=newone()
print tom.name

tom.eat()
tom.cc()
tom.ss()

newone.cc()

newone.ss()
#print tom.num
#tom._sleep()