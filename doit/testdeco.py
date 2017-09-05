
def login(func):
    def inner(arg):
        print "login good!!"
        func(arg)
    return inner



@login
def tv(name):
    print "welcome tv %s"%name


#tv=login(tv)
tv('tom')