#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/19 18:17
# @Author  : he.dongdong
# @Site    : 
# @File    : 04_迭代器_生成器_有序无序.py
# @Software: PyCharm





# 1,迭代器和生成器
# 几个概念：可迭代对象，迭代器，生成器

# 可迭代对象：
#        只要能被for循环遍历的(拥有iter方法)
# 迭代器：拥有iter，next()方法的，称为迭代器，
#        无next方法，但可以索引法迭代，称之为 -->序列（字符串，列表和元组）
#        无next，无索引法，为字典
# 生成器：拥有iter，next，yeild方法的
# ---->怎么生成迭代器


# 2，有序无序
#  读出/插入顺序是否一致：-->判断条件：是否可索引/下标法
#       有序对象:字符串,元组,列表
#
#       无序对象:字典,集合

'''
# 判断一个对象是不是iterable
import collections

isinstance(a, collections.Iterable)  # 直接判断
hasattr(a, '__iter__')  # 通常判断，也有可能没有__iter__函数但是有__getitem__函数，也是iterable。

# 判断一个对象是不是iterator
import collections

isinstance（a, collections.Iterator)
hasattr(a, '__next__')  # python3的判断，使用的是__next__()函数
hasattr(a, 'next')  # python2的判断，使用的是next()函数

# 创建一个迭代器对象
list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
print (next(it))   # 输出迭代器的下一个元素

'''


import collections

# int,float,str,bool
a = 1
a1 = 1.21
b = 'abc'
c = True
print (isinstance(a, collections.Iterable))
print (isinstance(a1, collections.Iterable))
print (isinstance(b, collections.Iterable))   # 字符串是可迭代对象，但不是迭代器
print (isinstance(c, collections.Iterable))

print (isinstance(a, collections.Iterator))
print (isinstance(a1, collections.Iterator))
print (isinstance(b, collections.Iterator))
print (isinstance(c, collections.Iterator))

# tuple,list,dict,set    -->全是可迭代对象(被for循环遍历)，但都不是迭代器，难道需要自己生成？
d = (1,2,4)
e = [1,2,5]
f = {'key':'value'}
g = {1,2,3}
print (isinstance(d, collections.Iterable))
print (isinstance(e, collections.Iterable))
print (isinstance(f, collections.Iterable))
print (isinstance(g, collections.Iterable))

print (isinstance(d, collections.Iterator))
print (isinstance(e, collections.Iterator))
print (isinstance(f, collections.Iterator))
print (isinstance(g, collections.Iterator))

# 验证set是否可被遍历：
for i in g:
    print(i)       # 事实证明可行


# 创建一个迭代器：
it = iter(e)
# print(hasattr(it, next()))
print(hasattr(it, '__next__'))  # 可直接判断类中是否存在该方法，或某个模块中是否存在该方法
print(next(it))             # 以此类推，迭代器最好用在类上
print(next(it))


if __name__ == "__main__":
    pass