
def get_num(num):
    tl=[]
    for i in num:
        
        if not isinstance(i,int):
            print "error"
            break
        
        if i%2==0:
            tl.append(i)
    print tl

#get_num([1,2,3,4,5,6,7,8,9,10])
get_num([1,2,3,4,5,6,7,8,9,10,"range"])    #how to make print not run,if have break????????????

        
#        
#def get_num2(num):
#	tl=[]
#	while True:
#		for i in num:
#			
#			if not isinstance(i,int):
#				print "error"
#				break
#			
#			if i%2==0:
#				tl.append(i)
#				
#	else:
#	    print tl
# 
#get_num2([1,2,3,4,5,6,7,8,9,10])
##get_num2([1,2,3,4,5,6,7,8,9,10,"range"])




import urllib

def get_page(url):
	g=urllib.urlopen(url)
	html=g.read()
	#return html
	with open("get_page.txt","w") as gg:
		gg.write(html)


url="http://www.ca.com"
#get_page(url)


def get_big(*num):
	tl=[]
	
	for i in num:
		tl.extend(i)
	print max(tl)
	
get_big([1,2,3],[4,5,6],[7,8,9,10000000])

#get_big([1,2,3],[4,5,6][7,8,9,10000000])  if comma is missing, TypeError: list indices must be integers, not tuple


import glob
import os
def get_dir(f):
	if os.path.exists(f):
		for i in glob.glob(f+'\*'):
			if os.path.isdir(i):
				get_dir(i)
				#print i  don't need it
			print i
	else:
		print "not dir"
#get_dir(r'd:\source')
get_dir(r'd:\source2017')
	