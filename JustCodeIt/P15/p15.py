
class Bird(object):
    __day=2018
    kind = 'justabird'
    def __init__(self):
        print "new Bird"
        self.hungry = True


    def eat(self,eatwhat):
        if self.hungry:
            print "eat %s" % eatwhat
            self.hungry = False
        else:
            print "thank you"

    def getday(self):
        return self.__day

    @classmethod
    def doit(self):
        print "just do it"

class SongBird(Bird):
    def __init__(self):
        #super(SongBird,self).__init__()
        Bird.__init__(self)
        self.kwz = 'jiji'


    def song(self):
        print "SongBird %s"% self.kwz

sb1= SongBird()
sb1.eat('nut')
sb1.eat('nut2')
sb1.song()

print sb1.getday()
print sb1.kind
sb1.doit()

Bird.doit()
print dir(Bird)
if "_Bird__day" in dir(Bird):

    print sb1._Bird__day

print issubclass(SongBird,Bird)
print isinstance(sb1,SongBird)
print isinstance(sb1,Bird)


print sb1.__class__, type(sb1)



class Member:
    count=0
    def __init__(self):
        Member.count +=1

m1=Member()
print m1.count

m2=Member()
print m2.count



class FilterClass:

    def __init__(self):
        self.block = []

    def filter(self,sequence):
        return  [x for x in sequence if x not in self.block]

class SpamClass(FilterClass):
    def __init__(self):
        self.block =['$']

fc1= FilterClass()
print fc1.filter([1,2,3])


fc2= SpamClass()
print fc2.filter([1,2,3,'$'])








class Birthday:
    def __init__(self,year,month):
        self.year = year
        self.month = month

class Course:
    def __init__(self,name, price):
        self.name = name
        self.price = price

class Teacher:
    def __init__(self,name,gender,birth,course):
        self.name = name
        self.gender = gender
        self.birth = birth
        self.course = course
    def teach(self):
        print "teaching..."

T1 = Teacher('T1','man',Birthday(2000,01),Course('python',10000))

print dir(T1)
print T1.birth.year
print T1.course.name




class Turtle:
    def __init__(self,x):
        self.num=x

class Fish:
    def __init__(self,x):
        self.num=x

class Pool:
    def __init__(self,x,y):
        self.turtle=Turtle(x)
        self.fish=Fish(y)
    def print_num(self):
        print ('pool guigui %d, fish %d'%(self.turtle.num,self.fish.num))

pool=Pool(1,10)
pool.print_num()





class People:
    def __init__(self,name, age, sex):
        self.name = name
        self.age = age
        self.sex =sex

class Course:
    def __init__(self,name, period, price):
        self.name = name
        self.period = period
        self.price = price

    def tell_info(self):
        print (self.name,self.period,self.period)

class Teacher(People):
    def __init__(self,name,age,sex,job_title):
        People.__init__(self,name,age,sex)
        self.job_title = job_title
        self.course = []
        self.students =[]

class Student(People):
    def __init__(self,name,age,sex,):
        People.__init__(self,name,age,sex)
        self.course =[]
        print ("i am a fresh--%s"%self.name)


tom = Teacher('tom',21,'boy','python')
jack = Student('jack',20,'boy')
python = Course('python',100,10000)
linux = Course('linux',30,6000)

tom.course.append(python)
tom.course.append(linux)

jack.course.append(python)
tom.students.append(jack)

for i in tom.course:
    i.tell_info()


