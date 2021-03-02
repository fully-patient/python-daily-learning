#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/23 14:51
# @Author  : he.dongdong
# @Site    : 
# @File    : 21_单例和设计模式_斐波那契数列.py
# @Software: PyCharm


# 设计模式：工厂模式和单例模式
# 单例应用场景：
#       资源共享的情况下，减少性能损失：如日志文件，应用配置等
#       方便资源之间通信：网站的计数器，多线程池，数据库配置/连接池，日志应用等
# 实现方式：(4种)
#       1，使用模块，2，使用__new__，3，使用装饰器，4，使用元类(metaclass)


# 1， 使用模块
#       python的模块就是天然的单例模式，
#               模块在第一次导入时，会编译一遍，生成.pyc文件，
#               在第二次导入时，会直接加载.pyc文件，不会再编译，不会再执行模块代码
class MySingle:
    def foo(self):
        pass

singleton = MySingle()

# 接着在另一文件中导入该对象实例就好了：
# 比如：from mysingle import singleton
#      singleton.foo()



# 2，使用__new__方法：
#       cls表示类，self表示实例
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

obj1 = Singleton()
obj2 = Singleton()
obj1.attr1 = 'value1'
print(obj1.attr1, obj2.attr1)
print(obj1 is obj2)         # 说明是同一个对象


# 3，装饰器方式：
def SingleTon_test(cls):
    instances = {}              # 用个字典去存
    def getinstance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args,**kwargs)    #直接创建对象，最后把这个对象返回
        return instances[cls]
    return getinstance              # 装饰器和闭包

@SingleTon_test
class myclass:
    a = 1
C1 = myclass()
C2 = myclass()
print(C1 is C2)


# 4，使用元类metaclass：元类可以控制类的创建过程，它主要做三件事：
#       拦截类的创建
#       修改类的定义
#       返回修改后的类
class Singleton2(type):     # type是什么东西，卧槽
    def __init__(self, *args,**kwargs):
        self.__instance = None
        super(Singleton2, self).__init__(*args,**kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super(Singleton2, self).__call__(*args,**kwargs)
        return self.__instance

class Foo(object):
    __metaclass__ = Singleton2      # 在执行到这时，元类中的new和init方法已经被执行了，而不是在Foo实例化时候执行，且仅会执行一次

foo1 = Foo()
foo2 = Foo()
print(Foo.__dict__)     # 对象的__dict__中存储了一些self.xxx的一些东西
print(foo1 is foo2)




# 斐波那契数列 [0,1,1,2,3,5]
def func_list(num):
    c_list = [0,1]
    for i in range(num-2):
        c_list.append(c_list[-2] + c_list[-1])
    return c_list




if __name__ == "__main__":
    pass