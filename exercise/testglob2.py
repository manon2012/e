import glob
import os


def getfilelist(f):
    tlist=[]
    for i in glob.glob(f+'\*'):
        print i
        if os.path.isdir(i):
            getfilelist(i)

        else:
           
            tlist.append(i)
            print i
    return tlist

print  getfilelist(r"d:\glob")

