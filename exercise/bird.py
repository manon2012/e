#! /usr/bin/env python
#coding=utf-8


class Bird:
    #hungry=True  error
    def __init__(self):
        print "create one"
        Bird.hungry=True  
        
    def eat(self):
        if Bird.hungry:
            print "eat le"
            Bird.hungry=False
        else:
            print "i am full"
            

class SongBird(Bird):
    def song(self):
        print "1234567"
        
        
class LookBird(Bird):
    def show(show):
        print "It's show time!"


s1=SongBird()
s1.song()
s1.eat()
s1.eat()
s1.eat()


l1=LookBird()
l1.show()
l1.eat()
l1.eat()