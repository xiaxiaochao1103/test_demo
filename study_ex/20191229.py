#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 9、有一个ip.txt，里面每行是一个ip，实现一个函数，ping 每个ip的结果，
# 把结果记录存到ping.txt中，格式为ip:0或ip:1 ，0代表ping成功，1代表ping失败
# import os
#
# with open("/Users/xiaxiaochao/PycharmProjects/untitled4/ssss/ip.txt", 'r', encoding="utf-8") as fp_obj:
#     lines = fp_obj.readlines()
#
# for line in lines:
#     flag = 1
#     ip = line.strip()
#     commandLine = os.popen("ping %s -c 3" % ip).read()
#     print(commandLine)
#     if "Request timeout" not in commandLine:
#         flag = 0
#     with open("/Users/xiaxiaochao/PycharmProjects/untitled4/ssss/ping.txt", 'a', encoding="utf-8") as fp_obj:
#         fp_obj.write("%s:%s\n" % (ip, flag))

# 10、删除无重复元组中给定的元素
# t = (1, 2, 3, 4, 5)
#
#
# def tuple_del(i, item):
#     list_item = list(item)
#     list_item.remove(i)
#     res = tuple(list_item)
#     return res
#
#
# print(tuple_del(2, t))


# 11.实现DOS命令执行功能，接受输入命令并执行，然后把执行结果和返回码打印到屏幕
# import os
#
#
# def print_command(command):
#     os.system(command)
#
#
# print_command("ls")


# 12.12、求一个n*n矩阵对角线元素之和
# n_lst = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]
#
# res_sum = 0
# for i in range(len(n_lst)):
#     for j in range(len(n_lst[i])):
#         if i == j:
#             res_sum += n_lst[i][j]
#         if i + j == 2:
#             res_sum += n_lst[i][j]
# print(res_sum)


# 13、输入一个数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组
# def exchange_num(lis):
#     max_index = 0
#     min_index = 0
#     print(lis)
#     for i in range(len(lis)):
#         if lis[i] > lis[max_index]:
#             max_index = i
#         if lis[i] < lis[min_index]:
#             min_index = i
#     print(lis[0], lis[max_index], lis[-1], lis[min_index])
#     lis.insert(len(lis), lis[min_index])
#     lis.insert(0, lis[max_index])
#
#     lis.pop(min_index+1)
#     lis.pop(max_index)
#     return lis
#
#
# lst2 = [1, 2, 3, 4, 89, 66, 5, 10]
# print("交换后的数组:", exchange_num(lst2))
