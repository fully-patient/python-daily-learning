#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/24 14:45
# @Author  : he.dongdong
# @Site    : 
# @File    : 23_正则表达式.py
# @Software: PyCharm


# 待写，后续有机会补充，这是个长期积累的过程ing

# https://www.runoob.com/regexp/regexp-syntax.html 很详细

# 暂时只写基本上用的的，时间紧急


# . 点号代表匹配除换行符（\n、\r）之外的任何单个字符，相等于 [^\n\r]
# + 加号代表前面的字符必须至少出现一次（1次或多次）
# ? 问号代表前面的字符最多只可以出现一次（0次、或1次）。
# * 星号代表前面的字符可以不出现，也可以出现一次或者多次（0次、或1次、或多次）
# {n,m} 代表前边的字符出现的次数m> .. >n
# \w 匹配字母、数字、下划线。等价于 [A-Za-z0-9_]
# \s\S 匹配所有。\s 是匹配所有空白符，包括换行，\S 非空白符，包括换行

#---------------------------------------------
# 例如1：^[0-9]+abc$
#       ^ 为匹配输入字符串的开始位置。
#       [0-9]+匹配多个数字， [0-9] 匹配单个数字，+ 匹配一个或者多个。
#       abc$匹配字母 abc 并以 abc 结尾，$ 为匹配输入字符串的结束位置。
#---------------------------------------------
# 例如2：^[a-z0-9_-]{3,15}$
#       ^ 为匹配输入字符串的开始位置。
#       [a-z0-9_-]：符合这些字符以内的。
#       {3,15}：字符的个数
#---------------------------------------------
#



# python的正则函数:
# re.match()：尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
#       re.match('^[0-9]$', str_a, flags=0)   # 从str_a上匹配对应的字符,匹配成功返回一个匹配的对象，否则返回None
#       re.match(xx).group(1)                 # 解析出对应的字符
# re.search()：扫描整个字符串并返回第一个成功的匹配
#       re.search('^[0-9]$', str_a, flags=0)  # 匹配成功返回一个匹配的对象，否则返回None
#       re.search(xx).group(1)                # 解析出对应的字符
# re.findall(r'目的字符串', '原有字符串')：在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。
#       注意：match和search是匹配一次，findall()是匹配所有

# re.sub()：检索和替换
#       re.sub('正则', '要替换成什么字符串', '原串', count=次数)
# re.compile()：转换成正则表达式对象，供match和search两个函数使用
#       pattern = re.compile('正则')
#       m = pattern.match(str_a)                 # 不需要再填正则了
#       m.group(0)
#       m.start(0)/end(0)                               # 获取字串在原串的位置
# re.split()：将字符串分割后返回列表
#       re.split('正则', '原串', maxsplit=0, flags=0)       # maxsplit默认为0，不限制次数



import re

#  match方法
print(re.match('com', 'www.runoob.com'))  # 为空的，注意，他只从第一个匹配
print(re.match('www', 'www.runoob.com'))  # 在起始位置匹配,返回的对象怎么处理？

line = "Cats are smarter than dogs"
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
if matchObj:
    print("matchObj.group() : ", matchObj.group())      # group()会返回元组内所有元素的拼接，
    print("matchObj.group(1) : ", matchObj.group(1))    # 后边加数字，就是元组中每一个值，()为一个界限用来区分
    print("matchObj.group(2) : ", matchObj.group(2))
    print("matchObj.groups() : ", matchObj.groups())    # 返回一个元组
else:
    print("No match!!")


# search方法
print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.search('com', 'www.runoob.com').span())         # 不在起始位置匹配

line01 = "Cats are smarter than dogs";

searchObj = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)

if searchObj:
    print("searchObj.group() : ", searchObj.group())
    print("searchObj.group(1) : ", searchObj.group(1))
    print("searchObj.group(2) : ", searchObj.group(2))
else:
    print("Nothing found!!")


# 替换
# 删除字符串中的 Python注释
num = re.sub(r'#.*$', "", '15156650035')
print("电话号码是: ", num)







if __name__ == "__main__":
    pass