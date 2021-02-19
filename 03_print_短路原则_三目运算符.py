#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/19 16:10
# @Author  : he.dongdong
# @Site    : 
# @File    : 03_print_短路原则_三目运算符.py
# @Software: PyCharm


# print的三种方式:
# 1，%(a,b) 替换
# 2，fstring
# 3，format

# 方式1：
a = 1
b = 'dongdong'
c = 2.113
print('hello world! value is %d,%s,%.2f'%(a,b,c), end='\n')


# 方式2：
print(f'hello world! value is {a}, {b}, {c},')     # 必须有f才能被正确认识到，还可以传函数，todo:暂时没找到只输出2位的那种

# 方式3：
print('hello world! value is {},{},{:.2f}'.format(a, b, c))  # format,必须前边有占位符,



# 短路原则：
# and：最后一个真和第一个假
# or：最后一个假和第一个真

a = 0
b = 1

print (a and b)
print (a or b)


# 三目运算符：
# c语言中的三木咋做到的？ python的三木怎么做到的？
# c语言的：条件表达式? case1;case2
# python的：case1 if 条件 else case2
print (a if a>b else b)


if __name__ == "__main__":
    pass