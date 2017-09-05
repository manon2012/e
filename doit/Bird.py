class Bird(object):
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print "eat"
            self.hungry = False
        else:
            print "no thanks"
        

class Birda(Bird):
    def fly(self):
        print "i can fly"

class Birdb(Bird):
    def __init__(self):
        #Bird.__init__(self)
        super(Birdb,self).__init__()
        self.sound = "jjzz"

    def sing(self):
        print self.sound


a=Birda()
a.eat()
a.eat()
a.fly()

b=Birdb()

b.sing()
b.eat()
b.eat()

