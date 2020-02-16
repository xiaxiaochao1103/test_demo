#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 86、找到某dict种包含指定key的dict.根据drink找到他的上级dict,即eat,并返回eat的内容
# dict_data = {
#     "name": "smith",
#     "age": 22,
#     "hobby": {
#         "read": "book",
#         "watch": "video",
#         "eat": {
#             "food": "中国菜",
#             "drink": "water",
#         },
#         "play": {
#             "game": "football",
#             "game1": "basketball"
#         }
#     },
#     "school": {
#         "a": 1,
#         "b": 2,
#         "c": 3,
#         "d": 4
#     }
# }
#
#
# def find_some_dict(d, key, result=None):
#     if result is None:
#         result = []
#     for k, v in d.items():
#         if k == key:
#             result.append(v)
#         else:
#             print(result)
#             if isinstance(v, dict):
#                 find_some_dict(v, key, result)
#     return result
#
#
# print(find_some_dict(dict_data, "eat"))


# 87、递归倒序打印1-10
# def print_num(n):
#     if n >= 1:
#         print(n)
#         print_num(n-1)
#
#
# print_num(10)


# 88、递归升序打印1-10
# def print_num(n):
#     if n >= 1:
#         print_num(n-1)
#         print(n)
#
#
# print_num(10)


# 89、把你知道的所有变量类型做一个赋值操作
# a = 1
# b = 'a'
# c = 1.5
# d = None
# e = 1 + 5j
# f = [1, 2, 3]
# g = (1, 2, 3)
# h = {'a': 1, 'b': 2}
# i = set([1, 2, 3, 4])
# j = ''
# k = True


# 90、请基于数字类型，使用2个数字分别实现+ - * / % //的操作
# x = 4
# y = 2
# print(x+y)
# print(x-y)
# print(x*y)
# print(x/y)
# print(x % y)
# print(x//y)


# 91、将一个字符串"0"，转换为数字类型，将1转换为数字类型
# a = "0"
# print(int(a))
#
# b = "1"
# print(int(b), float(b))


# 92、读入一个数字，并判断是否正数，是的话打印“是正数！”，否则打印“不是正数”
# num = int(input('请输入一个数字：'))
# if num > 0:
#     print('是正数')
# else:
#     print('非正数')


# 93、 随机产生一个整数，1-100范围内
# import random
# a = random.randint(1, 100)
# print(a)


# 94、 随机产一个小数，0-1内
# import random
# a = random.random()
# print(a)


# 95、随机产生一个小数，1-100内
# import random
# a = random.uniform(1, 100)
# print(a)


# 96、 随机产生一个字母，随机产生2个字母，随机产生3个字母。
# import random
# # 随机产生一个字母
# word = chr(random.randint(97, 122))
# print(word)
#
# # 随机产生两个字母
# for i in range(2):
#     word = chr(random.randint(97, 122))
#     print(word, end='')
# print()
# # 随机产生三个字母
# for i in range(3):
#     word = chr(random.randint(97, 122))
#     print(word, end='')


# 97、读入一个数字，判断是否奇数还是偶数。
# num = int(input('请输入一个数字：'))
# if num % 2 == 0:
#     print('它是偶数')
# else:
#     print('它是奇数')


# 98、 输入10个数字，算一下累加和
# numbers = input('请输入10个数字(以空格分开)：')
# num = numbers.split(' ')
# result = 0
# for i in num:
#     result += int(i)
#
# print(result)


# 99、 使用ASCII码 输出小写26个字母，a-z
# for i in range(97, 123):
#     print(chr(i), end="")


# 100、使用ASCII码 输出大写26个字母，A-Z
# for i in range(ord("A"), ord("Z") + 1):
#     print(chr(i), end="")


# 101、使用ASCII码 输出大小写26个字母，a-zA-Z
# for i in range(97, 123):
# #     print(chr(i), end="")
# #     print(chr(i - 32), end=" ")


# 102、从列表中随机取一个元素
# import random
# l = list(range(100))
# print(random.choice(l))


# 103、遍历一个列表[1,2,3,4,5,1]，请判断列表里面是否有1，有的话打印find it,没有的话提示，没有1.
# l = [2, 2, 3, 4, 5, 2]
# for i in l:
#     if i == 1:
#         print("find it")
#         break
# else:
#     print("not has 1")


# 104、遍历一个字符串"abdfsasd"，请判断列表里面是否有a，有的话打印find it,没有的话提示，没有"a"
# s = "abdfsasd"
# for v in s:
#     if v == "a":
#         print("find it")
#         break
# else:
#     print("not has a")


# 105、计算一个字符串"abdfsasd"有几个a
# s = "abdfsasd"
# print(s.count("a"))


# 106、输入高考的5个成绩，700
# 以上，打印可以上清华大学了，600 - -700
# 打印，可以上重点大学了，500 - -600
# 可以上一本了，400 - 500, 打印可以上大专了，400
# 以下打印请重头再来。


# 107、从1遍历到10，计算有几个偶数
# count = 0
# for i in range(1, 11):
#     if i % 2 == 0:
#         count += 1
# print(count)


# # 108、死循环从键盘输入内容，并打印，当输入“.”的时候退出循环
# while True:
#     cmd = input("请输入输入指令：")
#     if cmd == ".":
#         break
#     else:
#         print(cmd)


# 109、列表[1, 3, 5, 7, 9], 请将之拼接为一个字符串。
# lis = [1, 3, 5, 7, 9]
# print("".join([str(i) for i in lis]))


# 110、将"13579"的字符串转换为一个列表
# string = "13579"
# print(list(string))
# print([int(i) for i in list(string)])


# 111、将"13579"的字符串的数字求和一下
# string = "13579"
# print(sum([int(i) for i in list(string)]))


# 112、判断一个字符串是否包含非数字内容
# def is_digit_not_in(s):
#     for i in s:
#         if not i.isdigit():
#             print("包含非数字内容")
#             return True
#
#
# print(is_digit_not_in("1235d"))


# 113、写一个函数，实现两个数相加，函数参数a, b
# def add_num(a, b):
#     if isinstance(a, (int, float)) and isinstance(b, (int, float)):
#         return a + b
#     else:
#         print("参数错误")
#         return -1
#
#
# print(add_num(1, 4))
# print(add_num(1.3, 4))
# print(add_num(2, 4.5))
# print(add_num(2, "2"))

# 114、判断一个四位的数字，是否可以被2和5同时整除，如果可以打印可以整除，否则打印不可以整除
# def divisible_2or5(s):
#     if isinstance(s, (int, float)):
#         if s % 2 == 0 and s % 5 == 0:
#             print("可以整除")
#         else:
#             print("不可以整除")
#     else:
#         print("参数错误")
#
#
# divisible_2or5(10)
# divisible_2or5(9)
# divisible_2or5("10")

# 115、随机生成一个4位长度的整数数字，判断是否同事包含1和0
# import random
# s = "".join([str(random.randint(0, 9)) for i in range(4)])
# print(s)
# if "0" in s and "1" in s:
#     print("同时包含1和0")
# else:
#     print("未同时包含1和0")
#
#
# random_number = random.randint(1000,9999)
# print(random_number)
# if "1" in str(random_number) and "0" in str(random_number):
#     print("True")
# else:
#     print("False")


# 116、生成一个随机的8位密码，要求4个字母和4数字
# import string
# import random
# random_list = []
# for i in range(4):
#     random_list.append(str(random.randint(0, 9)))
#     random_list.append(random.choice(list(string.ascii_letters)))
#
# random.shuffle(random_list)
# print("".join(random_list))


# 117、求25这个数字可以整除的所有数字
# def divisible_list(num):
#     res = []
#     for i in range(1, num+1):
#         if num % i == 0:
#             res.append(i)
#     return res
#
#
# print(divisible_list(25))


# 118、 输入a, b, c三个数，求最大的那个
# a, b, c = 1, 2, 3
#
# if a < b:
#     a, b = b, a
# if a < c:
#     a, c = c, a
# if b < c:
#     b, c = c, b
#
# print(a, b, c)
# print(a)


# 119、 随机生成一个1 - 10的整数，然后你输入一个值去比对，如果大了，打印大了，小了打印小了，等于则打印。
# import random
# input_num = int(input("请输入一个1 - 10的整数："))
# random_num = random.randint(1, 10)
# print(random_num)
# if input_num > random_num:
#     print("大了")
# elif input_num < random_num:
#     print("小了")
# elif input_num == random_num:
#     print(random_num)


# 120、 基于第一题，限定一下猜的次数不超过3次
# import random
# for i in range(3):
#     input_num = int(input("请输入一个1 - 10的整数："))
#     random_num = random.randint(1, 10)
#     print(random_num)
#     if input_num > random_num:
#         print("大了")
#     elif input_num < random_num:
#         print("小了")
#     elif input_num == random_num:
#         print(random_num)


# 121、于第二题，打印一下一共猜了多少次。
# import random
# count = 0
# for i in range(3):
#     input_num = int(input("请输入一个1 - 10的整数："))
#     random_num = random.randint(1, 10)
#     count += 1
#     print(random_num)
#     if input_num > random_num:
#         print("大了")
#     elif input_num < random_num:
#         print("小了")
#     elif input_num == random_num:
#         print(random_num)
#
#
# print(count)


# 122、生成一个列表["1a", "2b", "3c", "4d", "5e"]
# res = []
# for i in range(5):
#     res.append(str(i + 1) + chr(97 + i))
#
# print(res)


# 123、生成一个列表["z1", "y2", "x3", "w4", "v5"]
# res = []
# for i in range(5):
#     res.append(chr(122 - i) + str(i + 1))
#
# print(res)


# 124、将一个字符串的奇数坐标的字母拼成一个字符串。
# s = "1sdkjlj111"
# print(s[1::2])


# 125、将一个字符串首字母、最后一个字母和中间字母，三个字符串拼成一个字符串。
# s = "abcde"
# result_str = s[0] + s[len(s)//2] + s[-1]
# print(result_str)


# 126、将一个列表[1,2,3,4,5]每个元素值扩大10倍后，在每个元素后面加上“abc”三个字母放到列表里面。
# lis = [1, 2, 3, 4, 5]
# for i in range(len(lis)):
#     lis[i] = str(lis[i] * 10) + "abc"
#
# print(lis)


# 127、两个列表[1, 2, 3, 4, 5], ["a", "b", "c", "d", "e"]，讲两个列表元素拼成一个字典，第一个列表元素做key，
# list1 = [1, 2, 3, 4, 5]
# list2 = ["a", "b", "c", "d", "e"]
# data = {}
# for i in range(len(list1)):
#     data[list1[i]] = list2[i]
#
# print(data)


# 128、一个字典{1:"a",2:"b",3:"c"}，拼成一个列表[1,"a",2,"b",3,"c"]
# data = {1: "a", 2: "b", 3: "c"}
# res = []
# for key, value in data.items():
#     res.extend([key, value])
#
# print(res)


# 129、使用for循环生成一个二维列表，[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# num = 1
# res = []
# for i in range(3):
#     temp_list = []
#     for j in range(3):
#         temp_list.append(num)
#         num += 1
#     res.append(temp_list)
#
# print(res)

# 130、将列表中[[1, 2, 3], [4, 5, 6], [7, 8, 9]]的所有奇数进行求和
# def sum_odd(para, res=0):
#     for i in para:
#         if isinstance(i, int):
#             if i % 2 == 1:
#                 res += int(i)
#         elif isinstance(i, (list, tuple)):
#             res += sum_odd(i)
#     return res
#
#
# lis1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# lis2 = [[1, 2, 3, [1, [1, 3]]], [4, 5, 6, [1.0, (1,)]], [7, 8, 9]]
# print(sum_odd(lis1))
# print(sum_odd(lis2))
