#! /usr/bin/env python
#coding=utf-8
def func_n4(url):
    s=url
    s1=s[s.index('?')+1:]
    print s1
    
    s2=s1.split('&')
    print s2
    """
    s2=['ie=utf-8', 'shb=1', 'src=360sou_newhome', 'q=python']
    
    d = [{'name': x[0], 'age': x[1]} for x in l]
    
    
    """
    print dict({s2})
    
    


url="https://www.so.com/s?ie=utf-8&shb=1&src=360sou_newhome&q=python"
func_n4(url)