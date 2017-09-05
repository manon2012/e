

def home():
    print "home"
    
def tv():
    #login()
    print "tv"
    
def ja():
    #login()
    print "ja"
    
    
def login(func):
    print "login module run"
    return func()
    
    
tv=login(tv)
tv()
    

#home()
#tv()
#ja()


def (${2:}):
    ${0}