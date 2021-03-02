#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/21 15:19
# @Author  : he.dongdong
# @Site    : 
# @File    : 16_函数_匿名函数.py
# @Software: PyCharm


# 函数：
#    作用：减少重复代码，登记
#    形参(顺序，不定长参数(位置:*args，关键字:**kwargs))，实参；
#    返回值
def func(a, b=2, *args,**kwargs):
    '''
    function: this fuc is just a test
    :return: none
    '''
    pass
    test_a = args
    test_b = kwargs
    print(a,b,test_a,test_b)
    print(test_a, *test_a)      # 不加*是元组，加了就是解包了？？
    print(test_b, *test_b)      # 不加是字典，加了就相当于解包：变成只有key的集合
    if 0!=1:
        return False
    elif 0 == 1:
        return True
    else:
        return (0,1,2)

return_value = func(1)
print(return_value)

test_value = func(1,3,(1,4,6),{'key':'value'})
test_value_2 = func(0,3,1,4,4,name='333',age=20)

# 函数的嵌套和递归调用：
#    递归：自己调用自己，要设置退出条件，不然死循环了

# 局部变量/全局变量：
#       函数内，需要用global声明全局变量
#       局部变量优先级高于全局变量：LEGB
#           L —— Local(function)；函数内的名字空间
#           E —— Enclosing function locals；外部嵌套函数的名字空间(例如closure)
#           G —— Global(module)；函数定义所在模块（文件）的名字空间
#           B —— Builtin(Python)；Python内置模块的名字空间



# lambda匿名函数
f = lambda x,y : x+y
print(f(2,3))

if __name__ == "__main__":
    pass