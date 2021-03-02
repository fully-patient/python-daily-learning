#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/23 16:37
# @Author  : he.dongdong
# @Site    : 
# @File    : 22_闭包和装饰器.py
# @Software: PyCharm


# 多个装饰器调用顺序：
# 装饰时：谁离我近，谁先走，
# 调用时：谁在外层，谁先走

# 闭包和装饰器，啥区别？  （其他语言也可以做类似的活，只不过需要更费劲些）
# 闭包的格式：
#      两个函数的嵌套
#      外层函数返回内层函数的引用（注意不是调用，也就是地址），虽然外层函数执行完了，但内层函数地址没回收，
#      一般外层函数传递参数
#   --> 内层函数应用 = 外层函数()
# 与普通函数的区别：外层函数参数会在内存中保留

# 注意：装饰器内参数不需要挨层去传入，因为不是当前去调用内部函数，调用被调用函数名时才会传参

# 装饰前的test函数地址，装饰后由func指向
# 装饰后的test，指向了call_func

def set_func(func):
    def call_func(*args, **kwargs):
        print('.......')
        return func(*args, **kwargs)              # （闭包和装饰器区别就在这，注意加上return，不然func如果有返回就返回不了）
    return call_func

@set_func
def test(*args, **kwargs):
    print('its my func')
    return args, kwargs


# 道德上，装饰器不会去更改原先函数参数和返回值(医生可以杀人，也可以救人)
# 顺序：穿脱秋裤大法

# 语法糖，@sum ---> test = set_func(test)

test(1,3)




# 装饰器传参：三个函数的嵌套 ()   !!!!!!!

def set_value(value):
    print(value, '装饰器传递的参数，模拟最外层的打印')      # first
    def set_fun(func):
        print('模仿外层函数的打印')                      # second
        def call_fun(*args, **kwargs):
            print('模仿内层函数的打印')                  # third
            return func(*args, **kwargs)
        return call_fun
    return set_fun

@set_value('dongdong')
def test01(*args, **kwargs):
    print('被装饰的函数调用了')                          # forth
    return args, kwargs

test01(2,3,a=1)




# 类装饰器：
# 类+括号 --> 调用init方法
# 实例对象+括号  --> 调用call方法

class SetFunClass(object):
    def __init__(self, func):
        print('模仿外层函数的打印')
        self.fun = func                                # 模仿函数装饰器的外层返回内层函数的引用
    def __call__(self, *args, **kwargs):
        print('模仿内层函数的打印')
        return self.fun(*args, **kwargs)               # 调用

@SetFunClass            # 等效于：test_class = SetFunClass(test_class)   [发现没，最终这个函数名其实就是一个对象]
def test_class(*args, **kwargs):
    print('被装饰的函数调用了')
    return args,kwargs

test_class()        # 对象()   -->调用call方法



# 类装饰器传参，注意查看调用顺序  !!!!!

class SetFunValueClass(object):
    def __init__(self, func):
        print('模仿外层函数的打印')                           # second
        self.fun = func
    def __call__(self, *args, **kwargs):
        print('模仿内层函数的打印')                           # third
        return self.fun(*args, **kwargs)

    @classmethod
    def set_value(cls,value):
        print(value, '装饰器传递的参数，模拟最外层的打印')       # first
        return cls


@SetFunValueClass.set_value('helloworld')
def test_class_value(*args, **kwargs):
    print('被装饰的函数调用了')                               # forth
    return args,kwargs

test_class_value()        # 对象()   -->调用call方法





if __name__ == "__main__":
    pass