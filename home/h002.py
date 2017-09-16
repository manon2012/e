class Person():
    "test fengzhuang"
    date = 2017

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.country = "China"
    
    def _p(self):   #how to add pamameter here?
        print "u can't see it."
    
    def showp(self):
        print self._p

    def show(self,content):
        print  "%s-%s-%s"%(self.name,self.age,content)
        """print  "%s-%s-%s"%(self.name,self.age,self.content)
AttributeError: Person instance has no attribute 'content'"""

    @staticmethod
    def ss():
        print "this is static method"

    @classmethod
    def cc(cls):
        print "this is class method"

p1= Person("tom",21)
p1.show("gotoschool")

p2= Person("jj",21)
p2.show("upup")


print Person.date
print p1.date

Person.ss()
Person.cc()
