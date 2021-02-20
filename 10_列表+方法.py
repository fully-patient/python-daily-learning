#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/20 16:41
# @Author  : he.dongdong
# @Site    : 
# @File    : 10_列表+方法.py
# @Software: PyCharm


# list的方法：
#  总览：增删改查(方法)，
#       能否遍历/迭代+索引， [ok]
#       是否可切片，        [ok]
#       是否可len和in方法   [ok]
#       是否可+和*         [ok]

a = ['1','2','3']

# 遍历，索引，切片
for i in a:
    print(i)
print(a[1])
print(a[::-1])

# len和in方法, +和*号：都可
print(len(a))
print(a + [1,2])
print(a * 2)
print(a)

# 增：append,extend,insert
a.append([1,2,3])  # 当一个整体存入
a.extend([1,2,3])  # 拆包操作，将里面的每一个元素写入
a.insert(2,'8')    # 指定下标位置，插入某一个元素
print(a)

# 删：pop,remove,del,clear
b = ['1','3','5','7']
b.pop()
b.pop(2)    # 下标，越界会报错
print(b)

b = ['1','3','5','7','3']
b.remove('3') # 会删除所有，还是只有一个--->只删除第一个
print(b)
del b[-1]
print(b)
b.clear()
print(b)

# 改：下标法
b = ['1','3','5','7','3']
b[0] = '0'
print(b)

# 查：index，count，in； 没有find方法
print(b.index('5'))
print(b.count('5'))
# b.find()
print(b)

# 排序：sort,reverse
b.reverse()     # 纯逆序，内部不会排的
print(b)
b.sort(reverse=True)   # 这个就是真正的排序，里面的全部排了
print(b)


if __name__ == "__main__":
    pass