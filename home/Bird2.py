class Bird(object):
    def __init__(self):
        self.hungry = True
    
    def eat(self):
        if self.hungry:
            print "i am eat"
            self.hungry = False
        else:
            print "3q"
    
class SongBird(Bird):
    # def __init__(self):
    #     self.hungry = True
    #     self.skill = "1234567"
    def __init__(self):
        super(SongBird,self).__init__()
        self.skill = "1234567"


    def song(self):
        print self.skill

bird = Bird()
bird.eat()

b1 = SongBird()
b1.eat()
b1.eat()
b1.song()

