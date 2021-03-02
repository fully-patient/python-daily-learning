#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/21 16:10
# @Author  : he.dongdong
# @Site    : 
# @File    : 17_高阶函数.py
# @Software: PyCharm
from functools import reduce

# 高阶函数：map,reduce,filter

print(map(lambda x:x^2, (1,2,3)))           # 映射，返回迭代器对象，必须实例化成list，或者遍历
print(list(map(lambda x:x^2, (1,2,3))))

print(reduce(lambda x,y:x+y , (1,2,3)))  # 先执行1+2，两者的结果再叠加最后一个值，整体的结果再输出

print(filter(lambda x: x//3, (1,2,3)))    # 返回迭代器对象
print(list(filter(lambda x: x//3, (1,2,3))))    # 只输出3，意味着只要前边条件的结果返回的是true，就输出该值


if __name__ == "__main__":
    pass