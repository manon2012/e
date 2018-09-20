聚合(aggregation)：指的是整体与部分的关系。通常在定义一个整体类后，再去分析这个整体类的组成结构。从而找出一些组成类，该整体类和组成类之间就形成了聚合关系。需求描述中“包含”、“组成”、“分为…部分”等词常意味着聚合关系。

组合(composition)：也表示类之间整体和部分的关系，但是组合关系中部分和整体具有统一的生存期。一旦整体对象不存在，部分对象也将不存在。部分对象与整体对象之间具有共生死的关系。

请看下面的代码。类组合，Computer实例对象不存在了，内部组合的Cpu实例也不存在。聚合Computer实例对象不存在了，从初始化方法传入的Cpu实例不属Computer实例对象存在不存在的影响。


#! /usr/bin/env python
# coding:utf-8

'''
类对象组合关系
'''


class Cpu(object):

    def __init__(self):
        self.type = '286'


class Computer(object):

    def __init__(self):
        self.cpu = Cpu()  # 包含CPu类的实例对象

    def __del__(self):
        print "Cpu by by!"

old_computer = Computer()
del old_computer


#! /usr/bin/env python
# coding:utf-8

'''
类对象聚合关系
'''


class Cpu(object):

    def __init__(self):
        self.type = '286'


class Computer(object):

    def __init__(self, cpu):
        self.cpu = cpu  # 有一个CPu类的实例对象

    def __del__(self):
        print "没有权力和Cpu by by!"

old_cpu = Cpu()
old_computer = Computer(old_cpu)
del old_computer