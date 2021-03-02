#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/26 15:07
# @Author  : he.dongdong
# @Site    : 
# @File    : 30_docker知识_启动mysql.py
# @Software: PyCharm


# 用docker启动mysql：https://www.cnblogs.com/sablier/p/11605606.html
# docker讲解(相当详细了)：https://yeasy.gitbook.io/docker_practice/introduction

# 项目中会遇到的：
#       将mysql，redis等用docker容器启动，项目远程连接这些容器
#       自己设计dockerfile，从基础镜像中构建属于项目的镜像
#       将当前环境配置(django/flask，以及各种版本的包，打包成一个docker镜像，以便多人开发)

# 几个概念：
#       镜像，容器，远端仓库(dockerhub，自己搭建)
#       分层存储
#       Copy-on-Write: 只有容器层是可写的，容器层下面的所有镜像层都是只读的

#       搜索：docker search mysql:latest --filter=stars
#       拉取：docker pull mysql:5.7    （本地没有就会去远端仓库查找）
#            docker images ls/ps -a
#            docker image inspect xxx   (查看详细信息)
#       启成容器：
#               docker run -dit -p 8012:80 -v /data:/data --name mynginx nginx bash
#               参数：-dit, -P, -v, -h, -d(后台) ,-e(环境变量), --name
#       查看容器：docker ps -a
#               docker container inspect 容器id
#       重启容器等：docker start/stop/restart/kill/rm 容器id
#       离开容器：exit
#       进入容器：docker exec -it 容器id bash
#       查看日志：docker logs -f (-t --tail 10) xxx
#       将已有容器做成镜像：docker commit 容器名 镜像名
#       给镜像打tag：docker tag ubuntu:15.10 runoob/ubuntu:v3
#       上传到远端仓库：
#               docker login
#               docker tag ....
#               docker push ....
#       设置自动启动：docker服务启动 + --restart=always
#               (如果已经启动的项目，则使用update更新：docker update --restart=always)
#               (一般写在yml文件中)https://www.bbsmax.com/A/kvJ3ylRpdg/
#       定时任务：
#               可以用crontab，也可以在yml中配置(参考京东自动签到的yml文件)


# 容器互联：
#       方式：link,network,bridge
#       例如：docker run -it --link dongdongtest5:web01 centos6-ssh /bin/bash
#            两个容器之间就能ping通了


# 公司实际应用：docker compose
#   为什么：
#          说白了，可以多个(django,postgresql)一起构建，并且互联，dockerfile做不到
#   安装：sudo curl -L "https://github.com/docker/compose/releases/download/1.24.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
#           （自己替换需要的版本）
#        修改权限：sudo chmod +x /usr/local/bin/docker-compose
#   yml文件和dockerfile文件：
#       Dockerfile 是拿来构建自定义镜像的，并没有直接生成容器。只是可以在运行镜像时运行容器而已。
#       做容器编排以部署环境，是使用 docker-compose.yml 文件进行的，里面可能会需要用到 Dockerfile 。
#   命令：
#       用的最多的是：docker compose up -d     (代替build命令)
#   yml文件参数详解：
#       build/image：
#           每个服务都必须通过 image 指令指定镜像或 build 指令（需要 Dockerfile）等来自动构建生成镜像。
#           image后加镜像，build后加dockerfile的文件位置
#   实战1：
#       version: '3.3'
#       services:
#           postgres:                               //容器1
#               image: simsuez/postgres:9.5         //从基础镜像开始，image 或者 build
#               ports:                              //映射端口
#                   - 5432:5432
#               volumes:
#                   - ./volumes/postgres:/var/lib/postgresql/data   //宿主机：容器内
#                   - /mnt/data/backup/postgres/release:/mnt/pg_backup
#                   - /etc/passwd:/etc/passwd:ro                    //用户组直接映射，不需要重新创建了
#               env_file: ./env/postgres.env
#               user:  1003:1003
#               restart: always

#           o-sztx:                                 //容器2
#               build: ./build/odoo/sztx            //build：指定dockerfile的位置，也可把build单独列出来，里面添加context参数等
#               command: start --load=web           //依赖顺序，下边两个容器启动完，才做当前容器
#                   - postgres
#                   - redis
#               ports:                              //映射端口
#                   - 127.0.0.1:3369:8069
#               links:
#                   - postgres:db
#               volumes:
#                   - ./volumes/sztx:/opt/odoo/data  //一般把最新的代码放这，重启容器就行
#               env_file: ./env/odoo/sztx.env        //获取环境变量
#               restart: always
#
#   实战2：
#       自己根据教程，用dockerfile和docker compose启一个django



# sudo docker pull mysql:5.7
# sudo docker images
# sudo docker run -p 3306:3306 --name mysql -e MYSQL_ROOT_PASSWORD=123456 -d mysql:5.7
# 如果要映射目录：duso docker run -p 3306:3306 --name mysql \
# -v /usr/local/docker/mysql/conf:/etc/mysql \
# -v /usr/local/docker/mysql/logs:/var/log/mysql \
# -v /usr/local/docker/mysql/data:/var/lib/mysql \
# -e MYSQL_ROOT_PASSWORD=123456 \
# -d mysql:5.7

# sudo docker exec -it mysql bash
# mysql -uroot -p123456



# docker根据dockerfile构建镜像：
#       注意：现在一般都用docker-compose来生成了，底下这个了解就行
#       dockerfile的基本结构：（直接举例）
#			FROM              这个镜像的妈妈是谁？（指定基础镜像）
#			MAINTAINER 告诉别人，谁负责养它？（指定维护者信息，可以没有）
#			RUN               你想让它干啥(执行啥命令)（在命令前面加上RUN即可）
#			ADD               给它点创业资金（COPY文件，会自动解压）
#			WORKDIR      我是cd,今天刚化了妆（设置当前工作目录）
#			VOLUME        给它一个存放行李的地方（设置卷，挂载主机目录）
#			EXPOSE          它要打开的门是啥（指定对外的端口）
#			CMD              奔跑吧，兄弟！（指定容器启动后的要干的事情）
#			COPY             复制文件
#			ENV               环境变量
#           ENTRYPOINT  容器启动后执行的命令
#               LABEL：用于为镜像添加元数据
#               ENV：设置环境变量
#               EXPOSE：指定于外界交互的端口
#               VOLUME：指定映射目录
#               WORKDIR：工作目录，类似于cd命令
#               USER:指定运行容器时的用户名或 UID，后续的 RUN 也会使用指定用户。使用USER指定用户时，可以使用用户名、UID或GID，或是两者的组合。当服务不需要管理员权限时，可以通过该命令指定运行用户。并且可以在之前创建所需要的用户
#               ARG：用于指定传递给构建运行时的变量
#               ONBUILD：用于设置镜像触发器
#       构建命令：docker image build -f /path/to/a/Dockerfile
#       dockerfile实例：
#               FROM mysql:5.7                          //指定基础镜像
#               MAINTAINER dongdong                     //维护者是谁
#               ENV PATH /usr/local/nginx/sbin:$PATH    //设置环境变量
#               ADD nginx-1.8.0.tar.gz /usr/local/      //文件放到当前目录，拷过去自动解压
#               ADD epel-release-latest-7.noarch.rpm /usr/local/
#               RUN rpm -ivh /usr/local/epel-release-latest-7.noarch.rpm
#               RUN yum install -y wget lftp gcc gcc-c++ make openssl-devel pcre-devel pcre && yum clean all
#               RUN useradd -s /sbin/nologin -M www     //执行命令
#               WORKDIR /usr/local/nginx-1.8.0          //相当于cd
#               RUN ./configure --prefix=/usr/local/nginx --user=www --group=www --with-http_ssl_module --with-pcre && make && make install
#               RUN echo "daemon off;" >> /etc/nginx.conf
#               EXPOSE 80                               //映射端口
#               CMD ["nginx"]                           //执行命令




if __name__ == "__main__":
    pass