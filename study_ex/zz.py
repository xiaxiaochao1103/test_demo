#!/usr/bin/python
# -*- coding: UTF-8 -*-


# !/usr/bin/python
# -*- coding: utf-8 -*-
# from multiprocessing import Process
# import os
# import time
#
#
# def sleeper(name, seconds):  # 任务函数
#     print("Process ID# %s" % (os.getpid()))
#     print("Parent Process ID# %s" % (os.getppid()))
#     # 仅支持在linux上,一个进程会有父进程和自己的ID，windows上就没有父进程id
#     print("%s will sleep for %s seconds" % (name, seconds))
#     time.sleep(seconds)
#
#
# child_proc = Process(target=sleeper, args=('bob', 5))
# child_proc.start()
# print("in parent process after child process start")
# print("parent process about to join child process")
# child_proc.join()
# print("in parent process after child process join")
# print("the parent's parent process: %s" % (os.getppid()))

# coding: utf-8
import multiprocessing
import time


def m1(x):  # 打印个平方值
    time.sleep(0.01)
    return x.x + x.y


class a:
    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == '__main__':
    # 生成了一个进程池，帮你生成进程
    # 当前机器的cpu核数：multiprocessing.cpu_count()
    print(multiprocessing.cpu_count())
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    i_list = [a(i, i * 10) for i in range(1000)]
    time1 = time.time()
    result = pool.map(m1, i_list)
    time2 = time.time()
    print('time elapse:', time2 - time1)
    print(result)

    time1 = time.time()
    list(map(m1, i_list))
    time2 = time.time()
    print("time elapse:", time2 - time1)
