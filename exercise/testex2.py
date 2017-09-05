

# with two try_exception

def testex2():
    try:
        g=open("jdread.txt","r")
        try:
            print g.read()
        except Exception,e:
            print "can't read it, maybe no access right"
        
        finally:
            g.close()
            print g.closed
    except Exception,e:            
        print "can't find this file."
        
    

testex2()