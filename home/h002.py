class Person():
    "test fengzhuang"
    date = 2017

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.country = "China"
    
    def __p(self):   #how to add pamameter here?
        print "u can't see it."
    
    def showp(self):
        #print self._p <bound method Person._p of <__main__.Person instance at 0x017EAA30>>
        self.__p()

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

class ChildPerson(Person):
    pass
    

p1= Person("tom",21)
p1.show("gotoschool")

p2= Person("jj",21)
p2.show("upup")


print Person.date
print p1.date

Person.ss()
Person.cc()

p1.showp()
#p1.__p()

cp1=ChildPerson("tt",21)
#cp1.__p() ChildPerson instance has no attribute '__p'
cp1.showp()  

p1._Person__p()
#Any identifier of the form __spam (at least two leading underscores, at most one trailing underscore) is textually replaced with _classname__spam, 
# where classname is the current class name with leading underscore(s) stripped.


print "#################"
__metaclass__ = type
class Bird():
    def __init__(self):
        self.hungry = True

    def eat(self):
        while self.hungry:
            print "i am eat"
            self.hungry = False
            print "test here can print"
            break
        else:
            print "thanks"

class ChildBird(Bird):
    def __init__(self):
        self.sound = "QuQu"
        super(ChildBird,self).__init__()
        """   super(ChildBird,self).__init__()
         TypeError: super() argument 1 must be type, not classobj
         two method:
         A. __metaclass__ = type
         B. class ChildBird(Bird,object)
         
         """
    
    def song(self):
        #print self.song() RuntimeError: maximum recursion depth exceeded
        print self.sound
    

cb1 = ChildBird()
cb1.eat()
cb1.eat()
cb1.song()

print "$$$$$$$$$$"

class f():
    def p(self):
        print "fp"
        self.testself()
    def testself(self):
        print "testself_f"

class ffa(f):
    def p1(self):
        print "ffa"
    def testself(self):
        print "testself_ffa"

class ffb(f):
    def p1(self):
        print "ffb"
    def testself(self):
        print "testself_ffb"

class fff(ffa,ffb):
    def testself(self):
        print "testself_fff"

fff1= fff()
fff1.p()
