
menu = {'a':{
             'a1': 1,
             'a2':2
          },
        'b':{
              'b1':1,
              'b2':2
        }
}

while True:
    for i in menu:
        print i
    choice = raw_input("please input your choice: ")

    if choice in menu:
        for i in menu[choice]:
            print i
    choice = raw_input("please input your new choice: ")