
menu = {'a':{
             'a1': {'a11':{}},
             'a2': {}
          },
        'b':{
              'b1':1,
              'b2':2
        }
}


current_layer = menu
flist=[]
while True:
    for key in current_layer:
        print key
    choice = raw_input(">>").strip()
    if choice in current_layer:
        flist.append(current_layer)
        current_layer = current_layer[choice]

    elif choice == 'q':
        break

    elif choice == 'qq':
        if flist:    
            current_layer=flist.pop() 

    