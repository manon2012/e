
def threetims():
    choice=raw_input("please sure: y or n:")
    try:
        if choice=='y':
            pass
    except TypeError:
        print "not y"
    else:
        print "ok"


threetims()