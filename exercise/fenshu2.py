

f= open(r"D:\git\e\exercise\fenshu.txt","r")
content = f.readlines()
print content   # ['a  10 20 30\n', 'b  15 15 15\n', 'c  20 10 20']

sum = 0
for i in content:
    sum = 0
    for ii in i.split()[1:]:
        sum += int(ii)
    print "%s's chengji is %s"%(i.split()[0], sum) 
    aa="%s's chengji is %s"%(i.split()[0], sum) 
    ff = open (r"D:\git\e\exercise\add.txt","a")
    print >> ff, aa
    ff.close()
    

    # print i.split()[0],
    # for ii in i.split()[1:]:
    #     sum +=int(i)
    # print sum



# alist =['a', '10', '20', '30']

# for i in alist[1:]:
#     sum=0
#     sum += int(i)
# print alist[0], sum



