#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 46、求1+2!+3!+...+20!的和。
# def factorial(num):
#     res = 1
#     if num == 1:
#         res = 1
#     else:
#         for i in range(1, num+1):
#             res *= i
#     return res
#
#
# def sum_factorial(num):
#     res = 0
#     if num == 1:
#         res = 1
#     else:
#         for i in range(1, num+1):
#             res += factorial(i)
#     return res
#
#
# print(sum_factorial(3))


# 利用递归方法求5!。
# def factorial(num):
#     res = 1
#     if num == 1:
#         return res
#     else:
#         return factorial(num - 1) * num
#
#
# print(factorial(4))


# 48、利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
# cmd = input("请输入5个字符：")
#
#
# def read_char(string,length):
#     if length == 0:
#         return
#     print(string[length-1], end="")
#     read_char(string, length-1)
#
#
# read_char(cmd, len(cmd))


# 49、有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。
# 问第4个人岁数，他说比第3个人大2岁。
# 问第三个人，又说比第2人大两岁。
# 问第2个人，说比第一个人大两岁。
# 最后问第一个人，他说是10岁。请问第五个人多大？
# def age(num):
#     ages = 0
#     if num == 1:
#         ages = 10
#         return ages
#     else:
#         return age(num - 1) + 2
#
#
# print(age(5))


# 50、给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
import random


def count_number(num):
    digit_count = 0
    for v in str(num)[::-1]:
        digit_count += 1
        print(v)
    print("数字的位数是: ", digit_count)


num = int("".join(random.sample("0123456789", random.randint(1, 5))))
print("num: ", num)
count_number(num)
