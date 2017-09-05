#coding=utf-8
import time
import datetime
import math
import test

def readmusic():
    with open ("love.txt","r") as f:
        listtime=[]
        listword=[]
        for line in f:
            listtime.append(line[1:9])
            listword.append(line[10:])
            
#            if line:
#                print line
#                time.sleep(1)
#                continue
        #print listtime
        #print listword
        
        #listtime=['00:18.83', '00:27.25', '00:34.68', '00:39.01', '00:43.10', '02:19.41', '02:27.87', '02:35.11', '02:39.41', '02:43.73', '02:46.29', '03:25.51', '03:30.21', '03:34.43', '03:37.24', '03:42.81', '03:47.10', '03:51.34', '03:54.21']
        listtime2=['00:01', '00:02', '00:3','00:01', '00:02', '00:3','00:01', '00:02', '00:3','00:01', '00:02', '00:3','00:01', '00:02', '00:3','00:01', '00:02', '00:3','00:01', '00:02', '00:3','00:01', '00:02', '00:3',]



#        def changetime(listtime2):
#            for i in listtime2:
#                aa=i.split(":")
#                print aa
#                return ((int(aa[0]))*60+ int(aa[1]))
        
        newnew=test.changetime(listtime2)
            
        #newtime=map(changetime,listtime2)
        
        #listt=[1,10,3]
        x=0
        for i in listword:
            print i
            
            #for x in range(len(listt)):
            time.sleep(newnew[x])
            x+=1
                
            #break

            
        
readmusic()