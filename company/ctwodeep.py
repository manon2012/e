
menu = {'a':{
             'a1': {},
             'a2':{}
          },
        'b':{
              'b1':{},
              'b2':{}
        }
}

# while True:
#     for i in menu:
#         print i
#     choice = raw_input("please input your choice: ")

#     if choice in menu:
#         for i in menu[choice]:
#             print i
#     choice = raw_input("please input your new choice, q for exit: ")
#     if 

currentlayer = menu
qlist = []

while True:
    for key in currentlayer:
        print key
    choice = raw_input(">>").strip()

    if choice in currentlayer:
        qlist.append(currentlayer)
        currentlayer=currentlayer[choice]
    if choice == 'r':
        if qlist:
            currentlayer = qlist.pop()
    if choice == 'q':
        break