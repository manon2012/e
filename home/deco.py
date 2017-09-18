
def outter(flag=""):
    def login(func):
        def wrapper(args):
            print "login haha"
            func(args)
            if flag=='true':
                print "with var"
        return wrapper
    return login

def home():
    print "home"
@outter('true')
def tv(jd):
    print ("tv %s")%jd
@outter()
def live(wx):
    print ("live %s")%wx

#tv=login(tv)


home()
tv('apple')
live('google')


