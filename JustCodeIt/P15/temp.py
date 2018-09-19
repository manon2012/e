
pepole = {
    'tom':{
        'phone':123456,
        'address': 'bj'
    }
    ,
    'jj':{
         'phone':654321,
        'address': 'usa'
        }
}

mapit = {
    'p':'phone',
    'add':'address'

}

print pepole

getwho = raw_input("please input name:")
if getwho in pepole:
    print "find it"
    newget = raw_input("what do you want, phone or add?")
    if newget =='phone':
        print pepole[getwho][newget]



        



