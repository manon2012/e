#import collections
#
#infile = open("myfile.txt")
#words = collections.Counter()
#
#for line in infile:
#    words.update(line.split())
#                              
#for word, count in words.iteritems():
#    print word, count
#


f=open("myfile.txt")

g=f.readline().split()
print g



gg=['If', 'you', 'are', 'using', 'Python','If','you','If']

a={}
for i in gg:
    print i
    a[i]= gg.count(i)

print a

value=a.values()
value.sort()
print value

for i in range(len(value)):
    print i, a[i]
    