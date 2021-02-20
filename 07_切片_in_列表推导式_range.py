#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/20 11:51
# @Author  : he.dongdong
# @Site    : 
# @File    : 07_切片_in_列表推导式_range.py
# @Software: PyCharm


# 切片三元素，顺序

# in：只要是可迭代对象(可被for循环遍历的)
a = 'helloworld'
if 'd' in a:
    print('I find it')

# range返回一系列的连续增加的整数，第三个参数：步长
# zip：并行迭代多个序列
a = dict(zip(['a','b','c'],(5,6,7)))
print(a)

# 列表推导式:
a = [i for i in range(0,20,1)]


if __name__ == "__main__":
    pass