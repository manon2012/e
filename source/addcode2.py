#! /usr/bin/env python
#coding=utf-8


import random, string

f = open('Promo_code.txt', 'wb')
for i in range(1):
    chars = string.letters + string.digits
    s = [random.choice(chars) for i in range(6)]
    f.write(''.join(s) + '\n')
f.close()
