

while True:

    try:
        # a='a'
        # a=int(a)
        a = input("please input a--->")
        a= int(a)
    except ValueError :
        print "got ValueError, continue..."
        continue
    except Exception as e:
        print "got Exception, continue..."
        print e
        continue

    if a>0 and a<5:
        print "normal"
        continue
    elif a >=5 and a <10:
        print "good"
        continue
    elif a==10:
        print "excellent"
        continue


