#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/20 19:19
# @Author  : he.dongdong
# @Site    : 
# @File    : 11_字典+方法.py
# @Software: PyCharm


# dict的方法：
#  总览：增删改查(方法)，
#       能否遍历/迭代+索引， [ok]，但是索引不行的
#       是否可切片，        [no]
#       是否可len和in方法   [ok]
#       是否可+和*         [no]


from collections import Iterable

dict_a = {'key':'value1'}

# 遍历/迭代？
for i in dict_a:
    print(i)   # 应该只有key
print(isinstance(i,Iterable))

# 切片，不允许
# len和in方法：
print(len(dict_a))
if 'key' in dict_a:    # in是可行的！！！
    print('i find it')

# +和* 方法：
# print(dict_a + {'key2': 'value2'})  # 直接报错，不能相加
# print(dict_a * 2)


# 增：dict[key]=xxx; update
dict_a['test'] = 'here'
dict_a.update({'test01': 222})          #必须字典结构，他会拆解
print(dict_a)

# 删：pop,popitem,del,clear
# dict_a.pop()   # 默认删除最后一个，但是总是提示需要参数
dict_a.pop('test')   # 通过key指定删除
dict_a.popitem()   # 不允许传参，默认就是删除最后一个键值对

dict_a = {'key':'value1','test01':123,'test02':234}
del dict_a['test02']   #只删除一个位置的
print(dict_a)
dict_a.clear()         #清空
print(dict_a)

# 改,查(两种方式):
dict_b = {'key':'value1','test01':123,'test02':234}
if dict_b.get('key'):
    dict_b['key'] = 'value01'
print(dict_b)


try:
    if dict_b['key2']:
        print('i find this')
except:
    print('报异常了')
finally:
    print(dict_b)



if __name__ == "__main__":
    pass