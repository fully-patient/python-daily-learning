#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/20 22:47
# @Author  : he.dongdong
# @Site    : 
# @File    : 15_异常和模块.py
# @Software: PyCharm
from jsonschema import ValidationError

# 异常:可接多个except

try:
    if 0 != 1:
        raise ValueError
except Exception as e:
    print(f'异常了,{e}')
except ValidationError as e:
    print('another validate error')
finally:
    print('ending!')


# 自定义异常：
#    只需要定义一个类
#    手动抛出这个类的实例，
#    拦截方法：这个类名
class MyOwnValidate(Exception):
    def __init__(self):
        pass
try:
    if 0 != 1:
        raise MyOwnValidate()
except MyOwnValidate as e:
    print('自定义异常成功')





if __name__ == "__main__":
    pass