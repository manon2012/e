#-*- coding: utf-8 -*-

a3cdict = { 'bj': {
                  'hd': {
                      '5daolou':{
                          'QingHua':{},
                          'BeiDa': {} 
                       },
                       'xizhimen':{},
                   },
                  'cy':{}
                  },
        
            'sh': {
                   'pd':{
                        'pd1':{
                            'aa':{},
                            'bb':{},
                          }
                    },
                    'px':{},
            } 
            
          }
# aa = {
#     '北京':{
#         "昌平":{
#             "沙河":["oldboy","test"],
#             "天通苑":["链家地产","我爱我家"]
#         },
#         "朝阳":{
#             "望京":["奔驰","陌陌"],
#             "国贸":{"CICC","HP"},
#             "东直门":{"Advent","飞信"},
#         },
#         "海淀":{},
#     },
#     '山东':{
#         "德州":{},
#         "青岛":{},
#         "济南":{}
#     },
#     '广东':{
#         "东莞":{},
#         "常熟":{},
#         "佛山":{},
#     },
# }

for k,v in a3cdict.items():
    print k,v

print a3cdict.keys()


while True:
    for k,v in enumerate(a3cdict):
        print k,v
    
    choice = raw_input("please enter your choice:")
    print a3cdict[a3cdict]