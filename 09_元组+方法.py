#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/20 16:18
# @Author  : he.dongdong
# @Site    : 
# @File    : 09_元组+方法.py
# @Software: PyCharm


# 元组的方法：
#  总览：增删改查(方法)，
#       能否遍历/迭代+索引， [ok]  (元组可以索引)
#       是否可切片，        [ok]
#       是否可len和in方法   [ok]
#       是否可+和*         [ok]

a = (1,'2',3)   #和list一样，可放不同数据类型

#遍历，迭代，索引？
for i in a:
    print(i)
print(a[2])
print(a[::2])
print(len(a))
print(a + (1,2))  #这是我没想到的
print(a*2)


# 组包和解包：
b = '1','2','3'
b1,b2,b3 = b


# 增  -->不行
a.__add__((4,2,3))  # 没生效，add方法不行
print(a)

# 删  -->只能删除整个，不能删除全部
del a

# 改  -->不行

# 查  -->index，count，无find方法
print(b.index('2'))
print(b.count('2'))
b.find('2')    #会报错

if __name__ == "__main__":
    pass