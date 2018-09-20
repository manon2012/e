# students=[{'id':001,'name':'tom'}]
#
# for i in students:
#     if i['id']==001:
#         print "got it"


s2 =[{'age': '21', 'id': 1, 'name': 'tom'},{'age': '21', 'id': 2, 'name': 'jj'}]

for i in s2:
    if i['id']==2:
        print "got one"
        i['id']=22
        print i


# print hasattr(s2[1],'age')

import os

print os.listdir('C:\Users\pei.wu\PycharmProjects\e\JustCodeIt\P15')
students =[]
with open('student.txt','r') as f:
    for line in f:
        print line
        students.append(line.strip().split(','))
print students

