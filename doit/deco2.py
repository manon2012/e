def outter(way="wx"):
    def login(func):
        def wrapper(args):
            if way== "wx":
                print "2017 wx logging"
                func(args) 
            else:
                print "jd logging"
                func(args) 
               
        return wrapper
    return login

#login()

@outter("wx")
def home(name):
    print "home,welocme %s"%name 

@outter("jd")
def live(name):
    print "live %s" % name

#home = login(home)

home("qq")
live("tt")