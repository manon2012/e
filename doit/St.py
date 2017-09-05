class Student(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age

class St(Student):
    def __init__(self,name,age,mail):
        #Student.__init__(self,name,age)  not wrok TypeError: __init__() takes exactly 2 arguments (4 given)
        super(St,self).__init__(name,age)
        self.mail=mail
    
    def updatemail(self,newmail):
        self.mail=newmail
        return self.mail
        

s1=Student("tom",21)
print s1.name
print s1.age

st1=St("jack",21,"mail")
print st1.mail

st1.updatemail("mail2")
print st1.mail


