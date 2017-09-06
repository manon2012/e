class Student(object):
    def __init__(self, name, age):
        self.n = name
        self.a = age
        self.c = "bj"


class newStudent(Student):
    def __init__(self,name,age,email):
        super(newStudent,self).__init__(name,age)
        self.e = email
    def updatemail(self, newmail):
        self.e=newmail

s1=Student("tom",21)
print s1.n
print s1.a
print s1.c

s2= newStudent("jack",22,"email")
print s2.n
print s2.a
print s2.c
print s2.e

s2.updatemail("eemail")
print s2.e




