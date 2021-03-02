#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/21 21:51
# @Author  : he.dongdong
# @Site    : 
# @File    : 19_导包_os模块.py
# @Software: PyCharm

# 导包方式两种：(xxx:模块名，yyy：模块里的方法等)
#    import xxx      +    xxx.yyy  (调用时)
#    from xxx import yyy
#    from module import *

# 导包的顺序：LEGB(由里到外)
# 模块中的__all__作用：对导入限制，被导入模块若定义了__all__属性，则只有__all__内指定的属性、方法、类可被导入；若没定义，则导入模块内的所有公有属性，方法和类。
__all__ = ['log_action','temp_int_a']     # 写在文件顶部就OK

# 导入的实质： 把包里面的内容运行了一遍
#      -->最好在包里加入 if __name__=='__main__'，保证某些方法/变量只有在当前文件中生效



import os
import logging
logger = logging.getLogger(__name__)
from os import fchmod

# os模块，创建文件夹，或者文件等，暂时只列举常用的
# os.access(path, os.F_OK/os.W_OK)  # 检查路径是否存在/写权限
# os.path.exists(path)              # 判断路径是否存在
# os.path.basename(path)            # 返回文件名
# os.path.dirname(path)             # 返回文件夹路径
# os.path.abspath(path)             # 返回绝对路径
# os.listdir(path)                  # 罗列path底下所有的文件(包括文件夹)
# os.path.join(path1,path2)         # 两个路径拼接
# os.path.isfile(path)              # 判断这个路径是不是文件
# os.chmod(path, 0o666)             # 修改文件的权限，不一定能成功就是了
# os.mknod(path + '/' + file_name)  # 尝试创建文件
# os.path.split(path)               # 把路径分割成dirname，basename

temp_int_a = 234

path = r'/home/patient'
file_name =  'test_file.py'
log_info = 'file write test'
def log_action(self, log_info=''):
    '''
    functional: 根据路径，逐级往下查找文件，最终将log写入文件中
    :param self:
    :param log_information:
    :return:
    '''
    if os.access(path, os.F_OK):    # 判断路径是否是真实的
        print('路径是真实的')
        for file in os.listdir(path=path):      # 展示当前路径下的下一层
            final_path = os.path.join(path, file)   # 拼接下一层的路径
            if os.path.isfile(final_path) and file==file_name:
                if os.access(final_path,os.W_OK):   # 检查有没有写权限
                    try:
                        with open(final_path, 'a+') as f:
                            f.write(log_info.encode('utf'))   # 写入
                            # f.write(
                            #       log_info.encode('utf-8').decode('gbk').encode('utf')
                            #       )
                    except Exception as e:
                        logger.warning(
                            "can't write file %s, error message is %s" % (
                                final_path, e)
                        )
                    break       # 说明找到文件了，没必要继续向下了
                else:
                    logger.warning(
                        "file write permission error: %s, try to change permission " % final_path)
                            # 没写入的权限，尝试修改权限
                    try:
                        os.chmod(final_path, 0o666)  # try to change file's permission
                        log_action(log_info)        # 递归调用，如果修改权限失败就直接跳出了
                    except Exception as e:
                        logger.warning(
                            "can't change file permission:%s in path: %s " % (file_name, path))
                    break
        else:                           # for 循环遍历完，都没找到该文件，送一首凉凉，还是自己创建吧
            logger.warning(
                "can't find file:%s in path: %s ,will create one" % (file_name, path))
            try:
                os.mknod(path + '/' + file_name)  # try to create file
                log_action()
            except Exception as e:
                logger.warning(
                    "can't create file:%s in path: %s " % (file_name, path))        # 创建失败
    else:
        logger.warning(
            "path: %s does not exist " % path)  # todo:record log,path isn't exist
        # os.makedirs(path, mode=0777)                  # if file_path isn't exist ,try to create

# 调用
log_action(log_info)




if __name__ == "__main__":
    pass