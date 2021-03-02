#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/1 19:49
# @Author  : he.dongdong
# @Site    : 
# @File    : 29_mysql理论+命令.py
# @Software: PyCharm



# 关系型：oracle，mysql，postgresql，sqlite等
# 非关系型：redis，mongodb

# 结构：库：表：行列
#   对于图片,音频和视频等文件：不存储在数据库中，只存文件路径(可以在服务器中，也可在远程存储对象中)

# mysql：3306端口
# mysql可以自己做高并发，oracle比较稳定
#       高并发解决方案：redis做缓存，队列筛选，事务

# mysql中几种数据类型？
#   int，string，decimal，日期类型date，枚举enum

# 数据约束(对值的约束)：  (主键默认非空唯一外键)
# 主键
# 	primary key auto_increment
# 非空
# 	not null
# 默认
# 	default 默认值
# 唯一
# 	unqiue
# 外键
#   foreign key (本表字段) references 外表名(外表字段)

# mysql -u root -p 123456DD
# use 数据库名
# create database 数据库名 charset=utf8
# show databases
# select database()
# drop database 数据库名

# 创建表：
# create table xxx (字段 类型 (约束)，字段2)
# CREATE TABLE IF NOT EXISTS `runoob_tbl`(
#       `runoob_id` INT UNSIGNED AUTO_INCREMENT,`runoob_title` VARCHAR(100) NOT NULL,
#       `submission_date` DATE,
#       PRIMARY KEY ( `runoob_id` )
#       )ENGINE=InnoDB DEFAULT CHARSET=utf8;
# show tables()
# drop table xxx
# 增加字段，修改字段，删除字段 alter table xxx add/modify/change/drop column 列名
#                         alter table 主表 add foreign key (主表的字段) references 子表名 (子表字段)

# curd操作
#  insert into table_xxx (字段1，字段2) values (value1,约束)， (value2,约束)
#  update table_xxx set gender="女"，age=35 where id=5
#  逻辑删除: alter table 表名 add isdelete bit default 0
#  查：
#       select * from xxx;
#       select distinct num from xxx where 条件;
#       select count(nun) from xxx where 条件;
#       select * from A_table as  A inner join B_table as B  on A.name=B.name

# 条件：
#   > <
#   and or not
#   like
#   %
#   in
#   not in
#   between and
#   is null/ is not null

# 排序和限制：
#   order by xx desc/asc
#   limit 4,2   只展示4页，每页两个

# join和子查询(in)
#      select * from A_table as  A inner join B_table as B  on A.name=B.name
#      select * from A_table where cls_id in (select id from classes)


# 分组=行压缩,  前边的分组字段非必须要写
#    select count(*),group_concat(name) from table_name group by 分组字段 having 条件

# 自连接：
#   table_name as g1 inner join table_name as g2  on g1.name=g2.name

# 查询结果插入
#   insert into zibiao (name,address)  (select name1,address1 from fubiao)

# 减少重复的办法：
#   拆分成多个字段-->自连接
#   拆成多张表，外键相关联

# 事务：
#       特性：原子一致持久隔离  （两个行为不可分割，两端数据一致，上锁期间不允许其他操作，转账成功不允许回滚）
#       使用：begin/start transaction，commit，rollback
#       事务只针对数据(删除表和库，他无能为力)
#       仅innodb支持事务

# 索引：
#      加快查询，只针对数据量很大的，经常查询的列
#      添加索引：alter table 主表 add index 索引名(字段名)

# 三范式：
#      一个数据一个字段
#      表中必须有主键
#      一个对象一个表

# pycharm使用mysql：
#      from pymysql import connect
#       conn = connect(host='localhost', port=3306, database='jing_dong', user='root', password='mysql', charset='utf8')
#       cs1 = conn.cursor()
#       cs1.execute("select * from goods where id=1;")
#       data = cs1.fetchall()
#       cs1.close()
#       conn.close()



# python调用c，需要让他们生成so文件，我们再去调用


if __name__ == "__main__":
    pass