#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/20 12:05
# @Author  : he.dongdong
# @Site    : 
# @File    : 08_字符串+方法.py
# @Software: PyCharm


# 字符串的方法：
#  总览：增删改查(方法)，
#       能否遍历/迭代+索引， [ok]
#       是否可切片，        [ok]
#       是否可len和in方法   [ok]
#       是否可+和*         [ok]

# 切片
s = 'abcdefgh'
s1 = s[::-1]   # 实现倒序，不改变原串
s2 = s[-1:3:-2]  #从最后一个，往回搞，步长为2，问题：会逆序么？--->会的hxxf
print(s1,s2)

# 遍历，索引，len和in方法
for i in s:
    print(i)
print(s[3])
print(len(s))

# 增加：没有append，add这种的方法，可以用.join来拼接，或者加号
s3 = s + 'g'
s4 = s * 2
s5 = 'new'.join(s)
print(s3,s4,s5)

# 删除，没有pop，remove这种的方法,
#    方式1：可以采用replace或者strip的方法，又或者split方法，切割后再叠加
#    方式2：强转成其他类型(如list)，处理后再转回来，(万能方法：增删都可以)
temp_list = list(s)
temp_list.pop(temp_list.index('g'))  # 删除这个元素
print(temp_list)
print(str(temp_list))   # 这种方法转不成功
print(''.join(temp_list))

s.strip('g')     # 只能移除头尾，必须最后边
print(s)

new_s = s.replace('g','',1)  # 不改变原串
print(new_s)

# 修改：
#       修改指定的：下标法，replace，

# 查：
#      index: 返回下标，没有就报错
#      find：返回下标，没有就返回-1
#      rfind：同上
#      count：出现的次数，可以指定区间
#      startswith，endswith，isupper, isdigit, islower
print(s.index('g'))
print(s.find('g'))
print(s.count('g',0,-1))
print(s.startswith('a'))

# 对齐，去除空白，对齐
print(s.capitalize())  # 不会改变原
print(s)
print(s.strip('\r\n'))
print(s)
print(s.center(10))
print(s.ljust(20))

if __name__ == "__main__":
    pass