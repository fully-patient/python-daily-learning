#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/2 20:33
# @Author  : he.dongdong
# @Site    : 
# @File    : 31_ssl证书.py
# @Software: PyCharm
#


# ssh公私钥：
#      ssh-keygen: 生成.pub和.private文件

# letsencrypt生成免费的证书，3个月自动过期（我记得是两种模式，standalone 和 web）
#       生成：
#           先保证nginx打开，可以接到80端口
#           sudo certbot certonly --standalone -d suez-changzhou-release.sz-odoo.com
#       生成后修改nginx中文件参数：
#            ssl_certificate：
#                   /etc/letsencrypt/live/suez-taixing-release.sz-odoo.com/fullchain.pem
#       更新证书：
#           certbot renew --cert-name  xxx.com
#

# 防火墙：
#   sudo ufw status
#   sudo ufw disable/enable










if __name__ == "__main__":
    pass