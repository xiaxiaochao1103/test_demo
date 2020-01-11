#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 1.关于python保留几位小数，不进行四舍五入的方法
# import re
#
# print(re.search(r"\d+\.\d{3}", str(0.0555555555556)).group())


# 2.假设有10个锁仓货币，每天释放（即变为非锁仓状态）它的 1/180个货币，
# 我要计算每天的释放量和剩余量，结果保留小数点后4位，其余截掉当锁仓货币小于0.1的时候，程序结束
# def cut(num, c):
#     c = 10 ** c
#     return int(num * c) / float(c)
#
#
# def lockedposition(currency):
#     while currency > 0.1:
#         liberate = cut((currency / 180), 4)
#         currency = currency - liberate
#         print("释放币数为%s,剩余币数为%s" % (liberate, currency))
#         print("*" * 20)
#
#
# lockedposition(10.0000)


# 3.二分查找
# 前提：列表需要时有序列表
# 时间复杂度(x)：log n  #2**x =n
# 比如128个数字只需要查找7次，速度最快
#
# 算法：
# 每次都查找中间位置的元素，如果相等则返回
# 如果中间位置元素小于要查找的元素，则需要查找的元素在右边，更新最小位置low
# 如果中间位置元素大于要查找的元素，则需要查找的元素在左边，更新最大位置hign
# def binary_search(lis, item):
#     low = 0
#     high = len(lis)-1
#     while low <= high:
#         mid = (low+high)//2
#         guess = lis[mid]
#         if guess == item:
#             return mid
#         elif guess > item:
#             high = mid - 1
#         elif guess < item:
#             low = mid + 1
#
#
# number_list = [2, 5, 13, 21, 26, 33, 37]
# print(binary_search(number_list, 5))


# 4、选择排序
# 选择排序的时间复杂度 n * log n，速度比二分查找要慢
# 比如有4个元素的列表，时间复杂度位4*log4 = 4*2 = 8
# 每次在当前列表查找最小元素，需要查找4轮
# 方式一：
#
# 算法：
# 1、定义个查找最小元素的函数
# 2、遍历n次（n=数组长度），每次找出当前列表的最小元素放入一个新的列表，原列表最小元素删除

# 方法一：whlie循环
# def select_sort(lis):
#     res = []
#     while len(lis) > 0:
#         min_num = lis[0]
#         for i in lis:
#             if i < min_num:
#                 min_num = i
#         print(min_num)
#         lis.remove(min_num)
#         res.append(min_num)
#
#     return res


# 方法二：for循环
# def select_sort(lis):
#     res = []
#     temp_list = lis
#     for j in range(len(lis)):
#         min_num = temp_list[0]
#         for i in temp_list:
#             if i < min_num:
#                 min_num = i
#         print(min_num)
#         temp_list.remove(min_num)
#         res.append(min_num)
#
#     return res
#
#
# l = [4, 89, 234, 6546, 7657, 90.5]
# print(select_sort(l))


# 5、求10以内所有数字平方之和
# def sum_squares(n):
#     res = 0
#     for i in range(1, n+1):
#         res += i**2
#     return res
#
#
# print(sum_squares(10))


# 6、输出10行内容，每行的内容都是第一行10个，第二行9个，第三行8个。。。。最后一行1个星
# for i in range(10):
#     print("*" * (10 - i))


# for i in range(10, 0, -1):
#     print("*" * i)


# 7、输出9行内容，，第1行输出1，第2行输出12，第3行输出123，以此类推，第9行输出123456789
# 方法1：
# for i in range(1, 10):
#     if i == 1:
#         print("1")
#     else:
#         res = ""
#         for j in range(1, i + 1):
#             res += str(j)
#         print(res)


# 方法2：
# temp = "1"
# for i in range(2, 11):
#     print(temp)
#     temp += str(i)


# 方法3：
# string = "123456789"
# for i in range(1, 10):
#     print(string[:i])


# 8.计算2的20次方。不允许用**和pow()
# res = 1
# for i in range(20):
#     res *= 2
# print(res)


# 9、计算从1到1000以内所有能被3或者17整除的数的和并输出
# res = 0
# for i in range(1, 1001):
#     if i % 3 == 0 or i % 17 == 0:
#         res += i
# print(res)


# 10、计算从1到1000以内所有能同时被3，5和7整除的数的和并输出
# result = 0
# for i in range(1, 1001):
#     if i % 3 == 0 and i % 5 == 0 and i % 7 == 0:
#         result += i
# print(result)
