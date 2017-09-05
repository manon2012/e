#! /usr/bin/env python
#coding=utf-8
"""
1.请输出其内容。
2.请计算该文本的原始长度。
3.请去除该文本的换行。
4.请替换其中的字符"2012"为"2013"。
5.请取出最中间的长度为5的子串。


"""



def play_txt(a):
    a1=open(a)
    s1=a1.read()  
    
    print s1
    
    print len(s1)
    
    print s1.strip()
    
    print s1.replace('2012','2013')
    
    print "$$$$$$$$$$"
    
    s2=s1.split('\n')
    print s2
    print max(s2,key=len)

play_txt(r"d:\source\test.txt")
