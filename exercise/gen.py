#! /usr/bin/env python
#coding=utf-8

#a=[[1],[1,2],[1,2,3]]

#def gen():
#    for i in a:
#        for ii in i:
#            print ii
#    
#gen()


#
#def gen():
#    for i in a:
#        for ii in i:
#            yield ii
#    
#for i in gen():
#    print i
#
#
#
#
#
#
#def reverse_str(data):
#    for i in range(len(data)-1,0,-1):  #-1, -1  -1
#        yield data[i]
#        
#
##reverse_str('golf')
#
#for i in reverse_str('gold'):
#    print i
#    
#    
#    
#    
#list=[[1,2,3],[6,6,[2017,2017,2017]]]
#def creategen(list):
#    for i in list:
#        for item in i:
#            yield item
#            
#for i in creategen(list):
#    print i,
#    
#    
#
##defread_file(fpath): 
##   BLOCK_SIZE =1024
##   with open(fpath, 'rb') as f: 
##       whileTrue: 
##           block =f.read(BLOCK_SIZE) 
##           ifblock: 
##               yieldblock 
##           else: 
##               return
#
#
#print '\n$$$'

lista=[[1,2,3],[[6,6],[2017,2017,2017]]]

##import pdb
#def showlist(list):
#    for sublist in list:
#        print sublist
#        #pdb.set_trace()
#        for item in showlist(sublist):
#            print item
#            
##for i in creategen(list):
##    print i,
#
#showlist(lista)


#def showlist(ll):
#    for i in ll:
#        if isinstance(i, list):
#            print i
#        else:
#            print i
#showlist(lista)


def showlist(li):
    for i in li:
        if isinstance(i,list):
            for j in i:
                print j
        else:
            print i
            
showlist(lista)


for i in m:
	if isinstance(i,list):
		for j in i:
			print j
	else: print i结果
