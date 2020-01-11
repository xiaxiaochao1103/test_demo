#!/usr/bin/python
# -*- coding: UTF-8 -*-


# a = [
#
#     {"yoyo1": "123456"},
#
#     {"yoyo2": "123456"},
#
#     {"yoyo3": "123456"},
#
# ]
#
# for i in a:
#     for key, value in i.items():
#         with open("a.txt", "a", encoding="utf-8") as file:
#             file.write("%s,%s\n" % (key, value))

#
# a = [1, 3, 5, 7]
# a[0], a[1], a[2] = a[1], a[2], a[0]
# print(a)
# a.insert(3, a[0]).remove(a[0])
# print(a)


# def fibonacci(n):
#     if n == 1 or n == 2:
#         return 1
#     res = fibonacci(n-1) + fibonacci(n-2)
#     return res
#
#
# def fibonacci_list(n):
#     res = []
#     for i in range(1, n+1):
#         res.append(fibonacci(i))
#     return res
#
#
# print(fibonacci_list(4))


# s = "hello_world_yoyo"
# res_list = s.split("_")
# print(res_list)


# a = [1, 3, 5, 7, 0, -1, -9, -4, -5, -8]
# positive_count = 0
# negative_count = 0
# for i in a:
#     if i > 0:
#         positive_count += 1
#     elif i < 0:
#         negative_count += 1
#
# print(positive_count, negative_count)


# a = [1, 3, 5, 7, 0, -1, -9, -4, -5, -8]
# #
# # res_list = [i for i in a if i > 0]
# # print(res_list)


# a = [1, 2, 3, 4, 5]
# b = ["a", "b", "c", "d", "e"]
# c = []
# for i in range(len(a)):
#     c.append(b[i] + str(a[i]))
# print(c)

# flag = True
# while flag:
#     command = input("请输入邮箱地址或输入'Q'结束程序：")
#     if command == "Q":
#         print("输入结束！")
#         break
#     flag_at = (command.count("@") == 1) and (command[0] != "@") and (command[-5] != "@")
#     if flag_at and command.count(".") == 1 and ".com" == command[-4:]:
#         print("邮箱地址正确")
#         print("您可以继续输入")
#     else:
#         print("邮箱地址错误，请重新输入")
#         continue


# def fb(n):
#     res = []
#     for i in range(n):
#         if i == 0 or i == 1:
#             res.append(1)
#         else:
#             res.append(res[i-1] + res[i-2])
#     return res
#
#
# print(fb(4))
# import re
#
# while True:
#     command = input("请输入邮箱地址或输入'Q'结束程序：")
#     if command == "Q":
#         print("输入结束！")
#         break
#     re_list = re.split("@|\.", command)
#     if len(re_list) == 3 and re_list[0] != "" and re_list[-2] != "" and ".com" == command[-4:]:
#         print("邮箱地址正确")
#         print("您可以继续输入")
#     else:
#         print("邮箱地址错误，请重新输入")
#         continue


# while True:
#     command = input("请输入邮箱地址或输入'Q'结束程序：")
#     if command == "Q":
#         print("输入结束！")
#         break
#     split_list = command[:-4].split("@")
#     if len(split_list) == 2 and split_list[0] != "" and split_list[1] != "" and ".com" == command[-4:]:
#         print("邮箱地址正确")
#         print("您可以继续输入")
#     else:
#         print("邮箱地址错误，请重新输入")
#         continue
