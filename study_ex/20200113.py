#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 26、输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数，面试概率极高的题目
# import string
# s = "I am& a good, good boy 123 @!23 ab@"
# res = {}
# for i in s:
#     if i.isalpha():
#         res["alpha"] = res.get("alpha", 0) + 1
#     elif i.isdigit():
#         res["digit"] = res.get("digit", 0) + 1
#     elif i == " ":
#         res["space"] = res.get("space", 0) + 1
#     elif i in string.punctuation:
#         res["punctuation"] = res.get("punctuation", 0) + 1
#
#
# print(res["alpha"])
# print(res["digit"])
# print(res["space"])
# print(res["punctuation"])


# 27.3*3的矩阵的所有值为奇数的元素求和。
# l = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# res = 0
# for i in l:
#     for j in i:
#         if j % 2 == 1:
#             res += j
#
# print(res)


# 28、请利用循环一次对list中的每个名字打印出Hello,xxx!
# L = ['Bart', 'Lisa', 'Adam']
#
# for i in L:
#     print("Hello,%s!" % i)


# 29.我国现有13亿人口，设每年增长0.8%，编写程序，计算多少年后达到26亿？
# res = 13
# count = 0
# while res < 26:
#     res *= 1 + 0.008
#     count += 1
#     print(res, count)
#
# n = 1
# while True:
#     sum_num = 13 * (1 + 0.008) ** n
#     if sum_num >= 26:
#         print(n)
#         break
#     else:
#         n += 1


# 30、小明身高1.75米，体重80.5kg.请根据BMI公式（体重公斤数除以身高米数）
# 帮小明计算他的BMI指数，并根据BMI指数
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖 用 if-elif判断并打印结果：
# weight = 80.5
# height = 1.75
# if weight/height < 18.5:
#     print("过轻")
# elif 18.5 <= weight/height < 25:
#     print("正常")
# elif 25 <= weight/height < 28:
#     print("过重")
# elif 28 <= weight/height < 32:
#     print("肥胖")
# elif weight/height >= 32:
#     print("严重肥胖")


# 31.创建10个随机的偶数整数，并且计算一下所有这些偶数的和。
# import random
# result = 0
# for i in range(10):
#     random_number = random.randint(0, 100)*2
#     print(random_number, end=" ")
#     result += random_number
# print()
# print("和: ", result)


# 32、给定一个正整数，编写程序计算有多少对质数的和等于输入的这个正整数，
# 并输出结果。输入值小于1000。如，输入为10, 程序应该输出结果为2。
# （共有两对质数的和为10,分别为(5,5),(3,7)）
