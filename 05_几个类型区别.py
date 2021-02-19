#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/19 21:01
# @Author  : he.dongdong
# @Site    : 
# @File    : 05_几个类型区别.py
# @Software: PyCharm

# 几个区别：
# https://www.jianshu.com/p/5ede7fa96d83

# 列表：存储的是链表，有序，存储的是地址，支持倒序(用切片)
a = [1,2,3]
b = a[::-1]
print (b)

# 字典：本质是hash键，key值的选取必须是可被哈希的，无序和有序的理解(dict和orderdict)，set就是key的集合，只不过是去重了
c = {'key1':'value1'}

# list和set的区别：
#    存储方式不同：一个链表，一个哈希表
#    list读取和存快，

if __name__ == "__main__":
    pass