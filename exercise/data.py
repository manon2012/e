#coding=utf-8

import linecache

"""
fields=bid,uid,username,v_class,content,img,time,source,rt_num,cm_num,rt_uid,rt_username,rt_v_class,rt_content,rt_img,src_rt_num,src_cm_num,gender,rt_mid,location,rt_mid,mid,lat,lon,lbs_type,lbs_title,poiid,links,hashtags,ats,rt_links,rt_hashtags,rt_ats,v_url,rt_v_url
"""


# 前期准备，整理数据
data_keys = ('bid', 'uid', 'username', 'v_class', 'content', 'img', 'created_at', 'source', 'rt_num', 'cm_num', 'rt_uid', 'rt_username', 'rt_v_class', 'rt_content', 'rt_img', 'src_rt_num', 'src_cm_num', 'gender', 'rt_bid', 'location', 'rt_mid', 'mid', 'lat', 'lon', 'lbs_type', 'lbs_title', 'poiid', 'links', 'hashtags', 'ats', 'rt_links', 'rt_hashtags', 'rt_ats', 'v_url', 'rt_v_url')


dict1 = {data_keys[k]: k for k in range(len(data_keys))}

print dict1
print dict1['username']

"""
{'uid': 1, 'links': 27, 'rt_v_class': 12, 'hashtags': 28, 'rt_hashtags': 31, 'rt_links': 30, 'src_cm_num': 16, 'img': 5, 'lon': 23, 'mid': 21, 'content': 4, 'source': 7, 'location': 19, 'rt_bid': 18, 'rt_uid': 10, 'v_url': 33, 'username': 2, 'src_rt_num': 15, 'rt_num': 8, 'bid': 0, 'rt_ats': 32, 'lbs_title': 25, 'rt_mid': 20, 'lat': 22, 'lbs_type': 24, 'rt_content': 13, 'rt_img': 14, 'rt_username': 11, 'rt_v_url': 34, 'gender': 17, 'created_at': 6, 'poiid': 26, 'v_class': 3,'ats': 29, 'cm_num': 9}

"""
#
#with open ("t.txt","r") as g:
#    tlist=[]
#    for line in g:
#        print line
#        tlist.append(line)
#    print tlist


f = linecache.getlines('t.txt')
print f
"""
['"264345016313466880","28803555","\xa4\xc6\xa4\xf3\xa4\xb8\xa4\xe7\xa4\xa6","","","","2012-11-02 12:35:37","web","26597","","152963467","","","","","26597","","","264341471132528640","","264341471132528640","264345016313466880","","","","","","","","","","","","https://twitter.com/h_ototake/status/264341471132528640",
"https://twitter.com/mtenjo/status/264345016313466880"\n', '"264975031216513024","223056438","","","","","2012-11-04 06:19:05","TweetList!","","","","","","","","","","","","","","264975031216513024","","","","","","","","","","","","","https://twitter.com/umiushi_no_uta/status/264975031216513024"\n']
"""


lines = [x[1:-3].split('","') for x in f] 
#print lines
"""
[['264345016313466880', '28803555', '\xa4\xc6\xa4\xf3\xa4\xb8\xa4\xe7\xa4\xa6','', '', '', '2012-11-02 12:35:37', 'web', '26597', '', '152963467', '', '', '','', '26597', '', '', '264341471132528640', '', '264341471132528640', '264345016313466880', '', '', '', '', '', '', '', '', '', '', '', 'https://twitter.com/h_ototake/status/264341471132528640', 'https://twitter.com/mtenjo/status/26434501631346688'], ['264975031216513024', '223056438', '', '', '', '','2012-11-04 06:19:05', 'TweetList!', '', '', '', '', '', '', '', '', '', '', '', '', '', '26497503
1216513024', '', '', '', '', '', '', '', '', '', '', '', '', 'https://twitter.com/umiushi_no_uta/status/26497503121651302']]
"""


user= [x[dict1['username']] for x in lines]
print user
totaluser=len(set(user))
print totaluser

users=list(user)
print users


t201211=filter(lambda x: x[dict1['created_at']].startswith('2012-11'), lines)
print len(t201211)



days=set([x[dict1['created_at']].split(" ")[0] for x in lines])
print days

a=list(days)
a.sort()
print a
#tlist=[]
#for x in days:
#    tlist.append(x.split(" ")[0])
#print tlist



hours=[int(x[dict1['created_at']][11:13]) for x in lines]
#print hours
#hd={}
#for i  in hours:
#    hd[i] = hours.count(i)
#    
#print max(hd)


total_by_hour = [(h,hours.count(h)) for h in xrange(0,24) ]

total_by_hour.sort(key=lambda x:x[1], reverse = True)
print total_by_hour[0][0]

#hours = [int(line[keys['created_at']][11:13]) for line in lines]
#
#total_by_hour = [(h,hours.count(h)) for h in xrange(0,24) ]
#
#total_by_hour.sort(key=lambda k:k[1],reverse=True)



days=list(set([x[dict1['created_at']].split(" ")[0] for x in lines]))
days.sort()
print days

dateline_by_user = {k:dict() for k in days}
print dateline_by_user
#{'2012-11-04': {}, '2012-11-02': {}}

print "$$$"
for line in lines:
    dateline = line[dict1['created_at']].split(" ")[0]
    username = line[dict1['username']]
    print line
    if 
        
        
    
    


#print dateline_by_user['2012-11-02']
#
#aa={'bb': {'tom':2}, '2012-11-02': {}}
#print aa['bb']['tom']
#aa['bb']['jj']=3
#print aa['bb']