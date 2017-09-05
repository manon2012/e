#! /usr/bin/env python
#coding=utf-8


"""
二：定义一个字典类：dictclass。完成下面的功能：
dict = dictclass({你需要操作的字典对象})
1 删除某个key
del_dict(key)
2 判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found"
get_dict(key)
3 返回键组成的列表：返回类型;(list)
get_key()
4 合并字典，并且返回合并后字典的values组成的列表。返回类型:(list)
update_dict({要合并的字典})

"""

class dictClass(object):
    
    def __init__(self,dict):
        self.dict=dict
        
    
    def del_dict(self,key):
        del self.dict[key]
        
    def get_dict(self,key):
        if self.dict.has_key(key):
            print self.dict[key]
        else:
            print "not found"
            
    def get_key(self):
        print self.dict.keys()
        
    def get_value(self):
        print self.dict.values()
    
        
        
    def update_dict(self,newdict):
        return self.dict.update(newdict)
       
    
    
a=dictClass({'qq':22,'yy':44})

print a


a.get_dict('qq')
a.get_key()
a.get_value()
a.del_dict('qq')
a.get_key()

#newdict={'aa':11}
b=a.update_dict({'aa':11})
print b





    
        