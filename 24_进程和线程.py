#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/24 22:38
# @Author  : he.dongdong
# @Site    : 
# @File    : 24_进程和线程.py
# @Software: PyCharm


import os
import time
from multiprocessing import Process, Pool
from time import  ctime,sleep
import threading
import multiprocessing

# https://www.cnblogs.com/lanyinhao/p/9223301.html

# 单任务和多任务：
# 多任务是线程完成的，进程是一个假象
#   cpu只认识线程，让cpu调度最小的是一个线程（运行计算依靠线程(干活的)）
#   进程是内存里的 （申请内存依靠进程(房间)）
#   ---->因此，程序需要一个进程，里面最少一个线程

# 并发和并行：
#       并发：交替运行(时间片)
#       并行：真正同时进行
# 如果任务数>cpu核数，并发
# 如果任务数<cpu核数，并行

# 每次创建进程，都自带一个线程
# 传参
# 进程稳定性比线程好
# kill -9杀死的都是进程
# 进程之间不共享全局变量（但会复制主线程资源），也可以使用队列,管道等方式他共享(由于内存块区分，所以不共享全局变量)
# 主进程会等待所有子进程执行结束再结束，如果主进程被强行杀死，子进程会结束，但资源不会回收(僵尸进程)
# 生成：
#   os.getpid()
#   Process(target=xxx,args=xx)
#   os.fork()
# 函数：
#   pid.start()
#   pid.join()
#   pid.terminate()

# 进程创建方式：3种：(fork，multiprocessing，进程pool)
# 方式1：
pid1 = os.fork()
if pid1:
    print('确实存在')
else:
    print('没创建成功')    # 很迷,这个地方
print('--------------------------')

# 方式2：
def run_proc(name):
    print('子进程运行中，name%s,pin=%d...'%(name,os.getpid()))
    time.sleep(10)
    print('子进程已经结束')

print('父进程%d.'%os.getpid())
pid2=Process(target=run_proc,args=('test'+multiprocessing.current_process().name,))  #提前创建子进程对象
print('子进程将要执行')
pid2.start()           # 子进程执行, process文件种有run和start方法
print('--------------------------')

# 方式3：
def worker(msg):
    print("%s开始执行,进程号为%d"%(msg, os.getpid()))
    time.sleep(1)
    print("%s执行完毕" % (msg))


pid3 = Pool(3)  # 定义一个进程池，最大进程数3
for i in range(10):
    # Pool.apply_async(要调用的目标,(传递给目标的参数元祖,))
    # 每次循环将会用空闲出来的子进程去调用目标,有空出来的就去调用
    pid3.apply_async(worker, (i,))      # 调用目标函数

print("----start----")
pid3.close()  # 关闭进程池，关闭后po不再接收新的请求
pid3.join()  # 等待po中所有子进程执行完成，必须放在close语句之后
print("-----end-----")
print('--------------------------')




# 程序自带一个主线程，主线程尽量不要调用方法，有方法/任务再开一个线程就行
# 线程之间无序(并行)，主线程会等待所有子线程结束，再结束

# daemon：守护主线程：(主人和仆人)
#           如果某个子线程的daemon属性为False，主线程结束时会检测该子线程是否结束，如果该子线程还在运行，则主线程会等待它完成后再退出；
#           如果某个子线程的daemon属性为True，主线程运行结束时不对这个子线程进行检查而直接退出，同时所有daemon值为True的子线程将随主线程一起结束，而不论是否运行完成。
#     两种方式：
#           threading.Thread(target=show_info, daemon=True)
#           线程对象.setDaemon(True)
# join：让主线程等待子线程：
#     线程对象.join()

# 线程之间共享全局变量-->但由于是并行的，可能导致全局变量出错(访问时数据可能没及时更新)
#     解决办法：
#            方式1：排队(相当于单线程)
#                  开启线程1
#                  主线程等待join
#                  开启线程2
#            方式2：互斥锁(同一把锁：互斥，不同的锁：没用)
#                  当线程1中代码没跑完，线程2来了，他会判断是不是和线程1的锁一样，如果一样，阻塞线程2，回到线程1


# 死锁：是指两个或两个以上的进程或线程在执行过程中，因争夺资源而造成的一种互相等待的现象，若无外力作用，
#       它们都将无法推进下去。此时称系统处于死锁状态或系统产生了死锁，这些永远在互相等待的进程称为死锁进程，
#       ---->及时释放，考虑充分
# 生成：
#       threading.Thread(func,args)/thread.start_new_thread(func,args)
# 函数：
#       threading.current_thread()  # 查看当前的线程
#       tid.start()
#       tid.join()
#       t2.setDaemon()


# 创建线程：
def music(func):
    print(threading.current_thread())
    for i in range(2):
        print('I was listening to %s. %s'%(func,ctime()))
        sleep(2)
        print('end listing %s'%ctime())
def move(func):
    print(threading.current_thread())
    for i in range(2):
        print('I was at the %s ! %s'%(func,ctime()))
        sleep(3)
        print('end moving %s' % ctime())

threads=[]
t1=threading.Thread(target=music,args=('星晴',))
threads.append(t1)
t2=threading.Thread(target=move,args=('正义联盟',))
threads.append(t2)
t3=threading.Thread(target=move,args=('test',))

#-----join（）------
# print(len(threads))
# for t in threads:
#     t.start()
#           # 果然是由于下边的这个导致的，又执行了一遍
# t2.join()#等价于t2.join，目的是为了最后执行最后一条打印信息，join 逐个执行每个线程，执行完毕后继续往下执行，
# print('--------------------------')
# sleep(2)

#------setdaemon()-------
t3.setDaemon(True)  #只守护t3，但不守护t1，t1会全部执行完，同时也会引发t3执行，但t3不会执行完，t1执行完，就退出
                    # 必须在线程start之前，就要设置
                    # 这里因为下边还有代码，主线程还没结束，所以需要屏蔽掉下边代码才能看到
threads.append(t3)
for t in threads:
    # t.setDaemon(True)#（执行一次后就退出）
    t.start()
print('--------------------------')


#-------互斥锁Mutex--------
def addNum():
    # 没加锁版本：
    # global num,lock #在每个线程中都获取这个全局变量
    # print('--get num:',num )
    # time.sleep(1)
    # num -= 1 #对此公共变量进行-1操作

    # 枷锁版本：
    global num,lock #在每个线程中都获取这个全局变量
    print('--get num:',num )
    time.sleep(1)
    lock.acquire()
    num -= 1 #对此公共变量进行-1操作
    lock.release()

num = 100  #设定一个共享变量
thread_list = []
lock = threading.Lock()     # 加锁版本
for i in range(100):
    t = threading.Thread(target=addNum)
    t.start()
    thread_list.append(t)

for t in thread_list: #等待所有线程执行完毕
    t.join()

print('final num:', num )      # 注：不要在3.x上运行，不知为什么，3.x上的结果总是正确的，可能是自动加了锁








if __name__ == "__main__":
    pass