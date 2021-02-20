#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/19 21:01
# @Author  : he.dongdong
# @Site    : 
# @File    : 05_数据类型区别和复杂度.py
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
#    存储方式不同：一个链表(占用空间少)，一个哈希表(因为只存key)
#    list存和操作比set慢，字典和set都是空间换时间
#    set主要是判断存在否
#    dict，hash函数+哈希桶。一个好的hash函数使到哈希桶中的值只有一个，若多个key hash到了同一个哈希桶中，称之为哈希冲突。
#    set就是一个简化的dict

# 时间复杂度：https://www.cnblogs.com/nxf-rabbit75/p/11669900.html
#    列表：获取，调用、修改，返回列表长度  -->o(1)
#    字典：hash，获取，删除，添加元素，in  -->o(1)
#    集合：in  -->o(1)
#    字符串：判断存在否，-->o(n) 因为他需要挨个遍历，最坏情况

if __name__ == "__main__":
    pass