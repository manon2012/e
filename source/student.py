#! /usr/bin/env python
#coding=utf-8


"""
一：定义一个学生类。有下面的类属性：
1 姓名
2 年龄
3 成绩（语文，数学，英语)[每课成绩的类型为整数]
类方法：
1 获取学生的姓名：get_name() 返回类型:str
2 获取学生的年龄：get_age() 返回类型:int
3 返回3门科目中最高的分数。get_course() 返回类型:int
写好类以后，可以定义2个同学测试下:
zm = student(‘zhangming‘,20,[69,88,100])
返回结果：
zhangming
20
100
lq = student(‘liqiang‘,23,[82,60,99])
返回结果：
liqiang
23
99

"""


class Student():
    def __init__(self,name,age,*core):
        self.name=name
        self.age=age
        self.core=core
        
    def get_name(self):
        print self.name
    
    def get_age(self):
        print self.age  
      
    
    def get_course(self,*core):
#        a=self.core
#        print a
#        print max(a)
#        return max(a)
         b=[]
         for i in self.core:
            b.extend(i)
         print b
         print max(b)   

    
zm = Student('zhangming',20,[69,88,100])
zm.get_name()
zm.get_age()
zm.get_course()