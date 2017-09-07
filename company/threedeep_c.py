menu = { 'bj': {
                  'hd': {
                      '5daolou':{
                          'QingHua':{},
                          'BeiDa': {} 
                       },
                       'xizhimen':{},
                   },
                  'cy':{}
                  },
        
            'sh': {
                   'pd':{
                        'pd1':{
                            'aa':{},
                            'bb':{},
                          }
                    },
                    'px':{},
            } 
            
          }
while True:
    for i in menu:
        print i
    choice1 = raw_input("please input your choice:")
    if choice1 in menu:
        while True:
            for i in menu[choice1]:
                print i
            choice2 = raw_input("please input your choice:")
            if choice2 in menu[choice1]:
                while True:
                    for i in menu[choice1][choice2]:
                        print i
                    choice3 = raw_input("please input your choice:")
                    for i in menu[choice1][choice2][choice3]:
                        print i






