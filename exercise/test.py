

def changetime(list):
    tl=[]
    for i in list:
        aa=i.split(":")
#        print aa
#        return ((int(aa[0]))*60+ int(aa[1]))



        tl.append(((int(aa[0]))*60+ int(aa[1])))
    return tl


listtime2=['00:01','01:05', '00:10']


print changetime(listtime2)

#map(changetime,listtime2)
