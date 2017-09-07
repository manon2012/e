
menu = {'a':{
             'a1': {'a11':{}},
             'a2': {}
          },
        'b':{
              'b1':1,
              'b2':2
        }
}

# flag =True
# while flag:
#     for i in menu:
#         print i
#     choice = raw_input("please input your choice: ")
#     while flag:
#         if choice in menu:
#             for i in menu[choice]:
#                 print i
#             choice2 = raw_input("please input your new choice: ")
#             while flag:
#                 if choice2 in menu[choice]:
#                     for ii in menu[choice][choice2]:
#                         print ii
#                     choice3 = raw_input("please input your new choice: ")
#                 elif choice2 == 'q':
#                     flag = False
#                 else:
#                     flag = True
                    


flag = True
qflag = True
while flag and qflag:
    for key1 in menu:
        print key1
    choice1 = raw_input("1>>:").strip()
    if choice1 == 'b':
        flag = False
    if choice1 == 'q':
        qflag = False
    if choice1 in menu:
        while flag and qflag:
            for key2 in menu[choice1]:
                print key2
            choice2 = raw_input("2>>:").strip()
            if choice2 == 'b':
                flag = False
            if choice2 == 'q':
                qflag = False
            if choice2 in menu[choice1]:
                while flag and qflag:
                    for key3 in menu[choice1][choice2]:
                        print key3
                    choice3 = raw_input("3>>:").strip()
                    if choice3 == 'q':
                        qflag = False
                    if choice3 == 'b':
                        flag = False
                else:
                    flag = True    
        else:
            flag = True   
else:
    flag = True                     