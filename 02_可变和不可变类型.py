#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/19 15:18
# @Author  : he.dongdong
# @Site    : 
# @File    : 02_可变和不可变类型.py
# @Software: PyCharm


# 可变和不可变类型，区分方法：是否直接存的是地址(直接修改里面的数据)，add和__iadd__方法
# 可变：list，dict，set
# 不可变：int,float，string，tuple，bool

# int
a = 2
print (id(a))
a = a + 1
print (id(a))

# float
b = 2.1
print(id(b))
b = b + 1
print(id(b))

# string
c = 'abc'
print(id(c))
c = c + 'd'
print(id(c))

# bool
d = True
print(id(d))
d = False
print(id(d))

# tuple
e0 = [1,2,2]
e = (1,'2',e0)
print(id(e))
e0.append(3)   # 这种方式不对，是因为list导致的，因此元组本身还是不可变类型
print(id(e))

# list
f = [1,2,3]
print(f)
print(id(f))
f.append(4)   # 我傻了，这个函数没有返回值的
print(f)
print(id(f))

# dict
g = {'key1':1, 'key2':2}
print(g, id(g))
if g and g.get('key1'):
    g['key1'] = 3
print(g, id(g))

# set
h = {1,2,3}
print(h, id(h))
h.remove(3)
h.add(4)
print(h, id(h))
# print (h[0])   # TypeError: 'set' object does not support indexing

if __name__ == "__main__":
    print('list,dict,set都是可变数据类型')