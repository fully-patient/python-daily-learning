#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/20 22:03
# @Author  : he.dongdong
# @Site    : 
# @File    : 13_type，is，==.py
# @Software: PyCharm

# type
class A(object):
    def __init__(self):
        self.org = 2
class B(object):
    def __init__(self):
        self.org = 3
a = A()
b = B()
print(type(A))

c = [1,2,4]
d = [1,2,4]

# is和==区别
#   is：是否是同一个对象
#   ==：两者的值是否一样
# 只有数值型和字符串型的情况下，a is b才为True，当a和b是tuple，list，dict或set型时，a is b为False。
print(c is d)       # 说明两个id是不一样的
print(c == d)

print(isinstance(c, list))


if __name__ == "__main__":
    pass