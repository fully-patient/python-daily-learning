#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/20 20:20
# @Author  : he.dongdong
# @Site    : 
# @File    : 12_集合+方法.py
# @Software: PyCharm



# set的方法：     --->主要为了去重
#  总览：增删改查(方法)，
#       能否遍历/迭代+索引， [ok]，但是索引不行的
#       是否可切片，        [no]
#       是否可len和in方法   [ok]
#       是否可+和*         [no]

set_a = {'a','b','c'}

# 遍历，索引
for i in set_a:
    print(i)
# print(set_a[0])   # 不能使用下标
# print(set_a['a'])   # 也不能用key取，因为他不是对应none

# 切片：
# print(set_a[::-1])    # 不能使用切片

# len和in方法
print(len(set_a))

# +和*
# print(set_a + {'a'})
# print(set_a * 2)


# 增：add和update
set_a.add('new')
print(set_a)
set_a.update('new02')   # update会拆解里面的内容，相当于extend
print(set_a)

# 删：pop，remove，clear，del
set_a.pop()  # 难道删除最后一个？？[随机一个？]
print(set_a)
set_a.remove('new02')
print(set_a)
del set_a['a']
set_a.clear()

# 改：不能直接改，只能删除了，再增加
set_a = {'a','b','c'}
set_a.remove('a')
set_a.add('d')

# 查：index,find,count----->都没有




if __name__ == "__main__":
    pass