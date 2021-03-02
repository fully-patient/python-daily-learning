#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/1 16:13
# @Author  : he.dongdong
# @Site    : 
# @File    : 27_linux基础等.py
# @Software: PyCharm


# linux上命令(ls,pwd,cd, dir/file的)
#   alias
# 搜索：
#   文本：ls | grep 'xx' (必须用管道/文本结合)(管道代替ls> a.txt)
#        grep a.txt 'bxd'
#   文件：find ./  -iname 'xxx'
# 端口查看:
#   lsof -i :端口
#   ps aux|grep 端口/进程id
#   netstate -nap | grep 端口
# 查看日志：
#   tail -f -n 100 xxx.log  /tail -100f xxx.log
# 管道和重定向：
#   ls > a.txt 和 ls >> a.txt
# 软链接和硬链接：
#   ln -s xxx xxxx  (软，中间关系)
#   ln  xxx xxxx    (硬，对文件的copy，直接指向文件)
# 远程访问：
#   压缩和解压缩：
#       tar zcvf ./a.tar.gz ../a.txt  -r 循环压缩
#       tar zxvf ./a.tar.gz a.txt -C 指定路径
#       zip -r ./a.zip ../a.txt 循环压缩(文件夹里面的文件)
#       unzip a.zip A -d 目录/路径
#   管理用户及用户组：
#       whoami，sudo su，sudo+命令
#       passwd, passwd +用户名
#       which+命令
#       添加用户：useradd -m 用户 -g 用户组
#       删除用户：userdel -r 用户名
#       添加用户组：groupadd 用户组
#       删除用户组：groupdel 用户组
#   usemod -G 改写用户的组之后 如果用户同时属于多个组 那么最终只会属于一个组
#   而 gpasswd -a 则是将一个用户加入到另一个组 同时不改变用户原来的组；
#       制定默认组：usermod -g 用户组 用户
#       向其他组添加：usermod -G 用户组 用户
#       添加组成员：gpasswd -a 用户 用户组
#       删除组成员：gpasswd -d 用户 用户组
#   查看用户/用户组：
#       cat /etc/passwd
#       cat /etc/group
#       sudo kill -9 +pid号
#   权限设置：
#       chmod 777 a.txt   (rwx)
#   远程登录：
#       ssh 远端用户名@ip地址
#   上传和下载：
#       上传：scp 本机路径/文件 用户名@ip地址:/目标路径  -r
#       下载：scp 用户名@ip地址:/目标路径/文件  本机的指定路径 -r

#   vi编辑器：
#       三种模式
#       指令：
#           / 快速搜索
#           shift+g 跳到文本最后一行
#           两次g  跳到首行
#           撤销：u
#           恢复撤销：ctrl+r


# 查看所有映射端口：
#       netstat -lntup

















if __name__ == "__main__":
    pass