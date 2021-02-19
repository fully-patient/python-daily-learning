#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/3 14:29
# @Author  : he.dongdong
# @Site    : 
# @File    : 01_8种数据类型.py
# @Software: PyCharm


# 1, 几种数据类型？
# 整形，浮点，字符串，布尔，元组，列表，字典，集合。
a = int(1)
a1 = float(1.1)
b = str('fef')
c = bool(True)
d = tuple((1,1,1))
e = list([1,2,2])
f = dict({'key':123})

g = [a,a1,b,c,d,e,f]

def print_type(numer):
    print (numer,type(numer))
    print (id(numer))

for eachone in g:
    print_type(eachone)



if __name__ == "__main__":
    pass
    print ('Trust me, everything is gonna be ok!')



