
#coding=utf-8

import p4

"""
1.定义一个func(name)，该函数效果如下。
assert func("lilei") = "Lilei"
assert func("hanmeimei") = "Hanmeimei"
assert func("Hanmeimei") = "Hanmeimei"
'''

"""

def funcstr(name):
    assert isinstance(name, str)  and len(name)>1
    result=name.title()
    
    return result

    
print funcstr("hanmeimei")

    