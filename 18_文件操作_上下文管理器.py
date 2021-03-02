#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/21 20:15
# @Author  : he.dongdong
# @Site    : 
# @File    : 18_文件操作_上下文管理器.py
# @Software: PyCharm

# 文件操作命令：
#   open('文件路径/文件', 'rb')   # 一般用变量替换，各种模式：rb+，wb+，a+(追加模式写入)
#   f.read()
#   f.readlines()  # 返回一个列表，每一行都是一个数据
#   f.read(n)      # 读取多个字符

f = open('test_file.txt','r')
print(f.read())     # 会打印所有的数据
f.close()

f = open('test_file.txt','a+')  # w模式直接覆盖，a模式直接追加
f.write('test write function')
f.close()

# 更近一层，with管理，会自动关闭文件
with open('test_file.txt','r') as f:
    print('------')
    print(f.read())

# 用类方式，模拟with内的open方法
class myopen(object):
    def __init__(self, path='', method='r'):        # 生成对象时，传递参数
        self.path = path
        self.method = method
    def __enter__(self):                            # 上下文管理器协议，生成f对象
        self.file = open(self.path, self.method)
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):  # 自动关闭
        self.file.close()

with myopen('test_file.txt','r') as f:
    content = f.read()
print(content)



if __name__ == "__main__":
    pass