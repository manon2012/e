

class Foo:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print "%s age is %s"%(self.name, self.age)

    def __call__(self):
        self.show()
    
f1 = Foo("tom",21)
f1()


