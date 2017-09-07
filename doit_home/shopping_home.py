
product_list = [('iphone',5000),('ipad',3000),('imac',15000)]

money = int(raw_input("please enter your money:"))

# for i in shoplist:
#     print i
'''
('iphone', 5000)
('ipad', 3000)
('imac', 15000)
'''

shop_car = []
saving = money
for x,y in enumerate(product_list):
    print x,y

while True:
    choice = raw_input("please enter your choice,q for exit:")
    if choice.isdigit():
        choice = int(choice)
        if choice < len(product_list):
            if saving >= product_list[choice][1]:
                shop_car.append(product_list[choice][0])
                saving -=product_list[choice][1]
                print shop_car, saving
            else:
                print "not enough"

        else:
            print "enter correct number"

    elif choice == 'q':
        print shop_car
        break
    else:
        print "need a number"

