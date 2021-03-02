#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/22 15:55
# @Author  : he.dongdong
# @Site    : 
# @File    : 20_类_面向对象.py
# @Software: PyCharm


# 类的三大特性的理解：
#       封装：能直接使用类的方法，类里面怎么实现的(调不调用他继承的类的方法，这个我们不管)，类似于黑箱
#       继承：子类共享父类的公开方法和属性
#       多态：不同对象实例之间存在差异：比如属性，方法

# 过程与对象啥区别？
#       面向过程：更符合人的思维：把每一个动作细化
#       面向对象：黑盒子，封装好，更具通用性
#       两者区别：
#           过程：优点：性能比面向对象高，因为类调用时需要实例化，开销比较大，比较消耗资源;比如单片机、嵌入式开发、 Linux/Unix等一般采用面向过程开发，性能是最重要的因素。
#                缺点：没有面向对象易维护、易复用、易扩展
#           对象：优点：易维护、易复用、易扩展，由于面向对象有封装、继承、多态性的特性，可以设计出低耦合的系统，使系统 更加灵活、更加易于维护
#                缺点：性能比面向过程低

# 类的常见问题：
#       定义：可以不写object，命名遵循大小驼峰
#       创建对象，调用方法/属性
#       公有和私有属性/方法：前边加__，类内部可以访问私有属性和私有方法
#       内置方法：__init__，__new__，__exit__，__str__(调用对象打印)，__del__(减少引用计数)
#       self参数：相当于自己传入自己        (应该是不用管的)
#       动态绑定属性
#       类的复合：属性是另一个对象，此时，谁的方法谁调用
#       类的划分：模型类和功能类  (只属性/方法)

# 类的继承(基类和派生类)：
#       只能继承父类公有的属性和方法
#       如果现在类中没有指定方法(比如init/new等)，自动找寻父类的方法(多继承的话，由左向右)
#                       注意：-->参数也会传入父类方法中
#       子类调用父类的方法：
#               父类名.方法名(self,参数)
#               super(子类名, self).方法(参数)
#               super().方法名(参数)
#       子类重写父类的方法：(子类搞一个新的)
#       多继承怎么向上查找(钻石继承)：假设a->b->d，a->c->d  (也就是b和c是同水平线的)
#               super方法调用，先找b，后找c，最后a
#               父类名.方法调用，d-b-a，然后d-c-a
#       多层继承：(b,c)，谁写在前边，谁优先
#       mro顺序：类顺序在程序开始时，占位时已定下

# 这两个是装饰器，不要加(),
# 静态方法：需要加staticmethod装饰器，调用时，不需要cls和self，类和对象都可调用
# 动态方法：需要加classmethod装饰器，调用时需要传类名

class A:
    def __init__(self):
        self.age = 10     # 测试继承顺序
    def test_order(self):       # 测试继承顺序
        # return self.age
        return 123


class B(A):
    def __init__(self):
        super(B, self).__init__()
        self.age = 20
class C(A):
    def __init__(self):
        self.age = 30

    def test_order(self):       # 测试继承顺序
        # return self.age       # 之所以不行，是因为D传进来的时候，self就是D，D中确实没有这个属性
        return 234

    def __my_func__(self):
        return 'this is my own func'

    def cross_fire(self,new_a):
        return 'new_a'

class D(B, C):

    test_z = 0
                                        # 类中全局变量
    def __init__(self, temp_a, temp_b):          # b 为另一个对象
        self.test_a = temp_a                # 公有属性,动态绑定属性
        self.test_b = temp_b
        self.test_c = temp_b.age
        self.__test_d__ = self.test_a       # 私有属性
    def __new__(cls, *args, **kwargs):
        # return B.__new__()                  # 调用父类方法
        # return super(D,cls).__new__(cls, *args, **kwargs)         # 为什么这种方法就不行
        return super().__new__(cls)         # new方法会返回这个对象，不返回无法执行init方法


    def __str__(self):
        return 'hello word'
    def __del__(self):
        super().__del__()      # 尝试调用父类的方法删除

    def myfunc(self, test_c):
        B.myfunc(self,test_c)        # 三种调用方法
        super(D, self).myfunc(test_c)
        super().myfunc(test_c)

        print(f'this is my method, {test_c}')
        print(self.__my_func__())       # 如果没东西，说明父类的私有方法构造不成功

    def cross_fire(self, new_b):
        return 'new_b'

    def test_order01(self):
        return B.test_order(self)

    def test_order02(self):
        return super(D, self).test_order()

    @staticmethod
    def static_func():
        print('静态方法')

    @classmethod
    def class_func(cls):        # 必须要有cls这个参数，调用时，需要传类名
        print('静态方法')

b = B()
print(b.age)
d = D(1,b)
print(d)                # 返回str的内容
print(d.test_a, d.test_b, d.test_c, d.test_z)
d.zanshi = 100          # 原来没定义的，直接赋值属性，也是可以的
print(d.zanshi)
print(d.cross_fire(200))    # 父类方法重写

# 测试继承顺序
print(d.test_order01())
print(d.test_order02())

# 测试静态和动态
print(d.static_func())
print(d.class_func())  # 需要传类名


if __name__ == "__main__":
    pass