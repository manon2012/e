
def big(method):
    def outter(func):
        def wrapper(args):
            if method=="wx":
                print "this is wx login unit..."
                func(args)
            elif method=="jd":
                print "this is jd login unit..."
                func(args)
            
        return wrapper
    return outter

@big("jd")  #use "wx", not wx
def home(name):  
    print "home... %s"%name

def tv():
    print "tv..."

home("tom") #home=outter(home)
tv()

def test_str_parameter(name):
    print 'this is %s'%name

test_str_parameter("tom")