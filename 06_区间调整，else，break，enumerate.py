#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/20 11:25
# @Author  : he.dongdong
# @Site    : 
# @File    : 06_区间调整，else，break，enumerate.py
# @Software: PyCharm

# 调整区间：比如n的原区间是(0,5)，现在区间是(10-20) -->a=10,b=20
#              n%(b-a+1)+a

# enumerate:同时产生偏移和元素: (偏移：元素)
for i in enumerate(['a','b','c']):
    print(i)

# while和for中的break直接跳出，else是必须遍历完才执行，被中断不执行

a = 20
while a:
    a -= 1
    if a == -1:
        break       # 提前退出不会执行else
    else:
        continue
else:
    print('进入while的else中')

print('while finally its over')


for i in range(0,20,1):
    if i >21:
        break       # 提前退出不会执行else
    else:
        continue
else:
    print('进入for的else中')

print('for finally its over')


if __name__ == "__main__":
    pass