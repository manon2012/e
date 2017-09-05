import glob
import os
import pdb

#tlist=[]
def getfilelist(f):
    tlist=[]
    for i in glob.glob(f+'\*'):
        if os.path.isdir(i):
            getfilelist(i)
            #pdb.set_trace()
        if os.path.isfile(i):
            tlist.append(i)
            print i
    return tlist

#print dir(getfilelist)    
#print getfilelist.__name__    

    
if __name__=='__main__':
    
    print  getfilelist(r"d:\glob")

