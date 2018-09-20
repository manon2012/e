# -*- coding:utf-8 -*-
def showInfo():
    print("**************")
    print(" 学生管理系统")
    print(" 1.添加学生的信息")
    print(" 2.删除学生的信息")
    print(" 3.修改学生的信息")
    print(" 4.查询学生的信息")
    print(" 5.遍历所有学生的信息")
    print(" 6.退出系统")
    print("**************")
showInfo()
students =[{'age': '23', 'id': 3, 'name': 'bill'},{'age': '21', 'id': 1, 'name': 'tom'},{'age': '22', 'id': 2, 'name': 'jack'}]





#[{name:'tom',id:001,}]
while True:
    key = int(raw_input("select one,1-6:"))
    if key ==1:
        print "welcome to add subsystem, ready2add"


        while True:
            id = int(raw_input("id"))
            for i in students:
                if i['id']==id:
                    print "id exist"
                    break
            else:
                break

        name = raw_input("input name")
        age = raw_input("age")

        studentinfo ={}

        studentinfo['id'] =id
        studentinfo['name']=name
        studentinfo['age'] =age

        students.append(studentinfo)
        print students

    elif key ==2:
        print "welcome to delete subsystem"
        print "current student：",students


        while True:
            del_id = int(raw_input("select id you want to delete"))
            for i in students:
                if i['id']==del_id:
                    print "found it, will delete..."
                    students.remove(i)
                    print students
                    break

            # else:
            #     break
        print students

    elif key == 3:
        print "welcome to change subsystem"
        print students

        while True:
            change_id = int(raw_input("select id you want to change"))
            for i in students:
                if i['id']==change_id:
                    print "found it"
                    changeitem = int(raw_input("which item do you want to change? 1-id, 2-name, 3-age:"))
                    if changeitem ==1:
                        print "this will change id"

                        while True:
                            newid= int(raw_input("newid:"))

                            for i in students:
                                if i['id'] == newid:
                                    print "id exist, enter a newone"
                                    break
                            else:
                                i['id']=newid
                                print students
                                break
                    elif changeitem ==2:
                        print "this will change name"
                        new_name = raw_input("input new name:")
                        i['name']= new_name
                        print students


                    elif changeitem ==3:
                        print "this will change age"
                        new_age = raw_input("input new age:")
                        i['age']= new_age
                        print students


    elif key == 4:
        print "welcome to search subsystem"
        print students

        while True:
            search_id = raw_input("select id you want to search, q for exit")
            if search_id == 'q': break
            for i in students:
                if i['id'] == int(search_id):
                    print "found it"
                    while True:
                        seach_item = raw_input("which item do you want to seach?  name or age,q to quit:")

                        # if hasattr(i,seach_item):
                        #     print getattr(i,seach_item)
                        if seach_item=='q':break
                        print i[seach_item]

    elif key == 5:
        print "welcome to list subsystem"
        print students

        students.sort(key= lambda i:i['id'])
        print students
        for i in students:
            print i['id'] , ','+ i['name'] , ',' , i['age']

    elif key ==6:
        print "exiting..."
        break


