#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 131、{1:'a',2:"b",3:'c'}，将所有key的数字求和，将value的所有字符串拼接为一个字符串
# data = {1: 'a', 2: "b", 3: 'c'}
# res_sum = 0
# res_str = ""
# for key, value in data.items():
#     res_sum += key
#     res_str += value
#
# print(res_sum, res_str)


# 132、 {1:'a',2:"b",3:'c'}将key和value进行交换，生成一个新字典
# data = {1: 'a', 2: "b", 3: 'c'}
# new_dict = {}
# for key, value in data.items():
#     new_dict[value] = key
#
# print(new_dict)


# 133、把[1,2,3,4,5,6]转换为字典{1:2,3:4,5:6}
# data = {}
# lis = [1, 2, 3, 4, 5, 6]
# for i in range(0, len(lis), 2):
#     data[lis[i]] = lis[i + 1]
#
# print(data)


# 134、生成随机的10个整数，进行求和
# import random
# result = 0
# for i in range(10):
#     result += random.randint(1, 100)
# print(result)


# 135、[1,"a",2,"b",3,"c"]请将里面的所有字母保留，去掉所有数字
# import string
#
# lis = [1, "a", 2, "b", 3, "c"]
# for i in lis:
#     if str(i) in string.digits:
#         lis.remove(i)
#
# print(lis)


# 136、"8426"变为"4213"
# s = "8426"
# print(str(int(s)//2))


# 137、 写一个函数输入一个字符串，判断是否包含既不是数字也不是字母也不是_的字符，只要包含一个就返回false
# def func(s):
#     for v in s:
#         if not(v.isdigit() or v.isalpha() or v == "_"):
#             return False
#     return True
#
#
# print(func("123"))


# 138、将['a','b','M','N']，将所有小写字母变为大写字母，大写字母变为小写字母["A","B","m","n"]
# l = ['a', 'b', 'M', 'N']
# for i in range(len(l)):
#     if "a" <= l[i] <= "z":
#         l[i] = l[i].upper()
#     else:
#         l[i] = l[i].lower()
# print(l)


# 139、一个正整数，输出该正整数的阶乘的值
# num = int(input(">>"))
# res = 1
# for i in range(1, num+1):
#     res *= i
# print(res)


# 140、生成字符串”acegi”
# result_str = ""
# for i in range(ord("a"), ord("i") + 1, 2):
#     result_str += chr(i)
# print(result_str)


# 141、生成列表[“a”,”c”,”e”,”g”,”i”]
# result = []
# for i in range(ord("a"), ord("i") + 1, 2):
#     result.append(chr(i))
# print(result)


# 142、生成字典{“a”:1,”c”:3,”e”:5,”g”:7,”i”:9}
# d = {}
# for i in range(1, 10, 2):
#     d[chr(i + 96)] = i
# print(d)


# 143、将以上字典的key和value拼接成字符串，不能使用字符串连接符（+）
# d = {'a': 1, 'c': 3, 'e': 5, 'g': 7, 'i': 9}
# d_list = []
# for k, v in d.items():
#     d_list.append(k)
#     d_list.append(str(v))
# print("".join(d_list))


# 144、写一个函数，参数传入字符串”abc”,函数返回字符串“xyz”
# def func(s):
#     result_str = ""
#     for i in s:
#         result_str += chr(ord(i) + ord("x") - ord("a"))
#     return result_str
#
#
# print(func("abc"))


# 145、写一个函数，如果传入的是list，且list长度大于3，只保留前3个元素并返回；
# def func(p):
#     if isinstance(p, list) and len(p) > 3:
#         return p[:3]
#     else:
#         return -1
#
#
# print(func([1, 2, 3, 4, 5]))
# print(func("abc"))


# 146、用户输入”abc123”,程序返回”a321cb”
# s = input(">> ")
# result = s[0]
# for i in range(len(s) - 1, 0, -1):
#     result += s[i]
# print(result)


# 147、将[“wulaoshi”, ” is ”, ”a”, ”boy”]替换成[“wulaoshi”, ” is ”, ”good”, ”big””boy”]
# 148、统计“Youare, abeautifullGirl, 666! ”中数字和字母的总个数；
# import string
# s = "You are ,a beautifull Girl,666! "
# num_count = 0
# letter_count = 0
# for i in s:
#     if i in string.digits:
#         num_count += 1
#     elif i in string.ascii_letters:
#         letter_count += 1
# print(num_count, letter_count)


# 149、 用户输入一个内容，判断里面是否包含了数字。
# import string
#
#
# def is_contain_num(s):
#     for i in s:
#         if i in string.digits:
#             return True
#         else:
#             return False
#
#
# content = input(">>>")
# print(is_contain_num(content))


# 150、用户输入一个内容，判断一下输入内容的长度是否为5，是则打印是，否则打印否
# def judging_len(s, length):
#     if isinstance(length, int):
#         if len(s) == length:
#             return True
#         else:
#             return False
#     else:
#         print("输入参数错误")
#         return False
#
#
# content = input(">>>")
# print(judging_len(content, 5))


# 151、把一个字符串转换为元组
# a = "abc"
# print(tuple(a))


# 152、将一个字符串转换为字典，例如{"a": "A", "s": "m"......}
# a = "dahdkahjkh9382he21ej2bj"
# result_dict = {}
# for i in range(0, len(a), 2):
#     try:
#         result_dict[a[i]] = a[i + 1]
#     except IndexError:
#         result_dict[a[i]] = None
#
# print(result_dict)


# 153、请将a字符串的数字取出，并输出成一个新的字符串。
# a = "dahdkahjkh9382he21ej2bj"
# res = ""
# for i in a:
#     if i.isdigit():
#         res += i
#
# print(res)


# 154、统计a字符串出现的每个字母的出现次数（忽略大小写，a与A是同一个字母），并输出成一个字典。 例{'a': 3, 'b': 1}
# a = "dahdkhjKh9382he2A1ej2bJ"
# d = {}
# for i in a:
#     if i.isalpha():
#         d[i.lower()] = d.get(i.lower(), 0) + 1
#
# print(d)


# 155、请去除a字符串多次出现的字母，仅留最先出现的一个, 大小写不敏感。
# 例'aAsmr3idd4bgs7Dlsf9eAF'，经过去除后，输出'asmr3id4bg7lf9e'
# a = "aAsmr3idd4bgs7Dlsf9eAF"
# res = ""
# for i in a:
#     if i.isalpha():
#         if i.lower() not in res:
#             res += i
#     elif i.isdigit():
#         res += i
#
# print(res)


# 156、按a字符串中字符出现频率从高到低输出到列表，如果次数相同则按字母顺序排列。
# a = "aAsmr3idd4bgs7Dlsf9eAF"
# d = {}
# result = []
# for v in a:
#     d[v] = a.count(v)
#
#
# def func(d):
#     max_value = max(d.values())
#     for k, v in d.items():
#         if v == max_value:
#             return k
#
#
# print(d)
#
# for i in range(len(d)):
#     result.append(func(d))
#     d.pop(func(d))
# print(result)


# 157、将所有的字符串变化为后一个字符串，比如“a”变成b，"z"变成A
# def func(p):
#     if "a" <= p <= "y":
#         return chr(ord(p) + 1)
#     else:
#         return chr(ord(p) - 25)
#
#
# print(func("a"))
# print(func("z"))


# 158、删除最开始一个字母、最后一个字母和中间的2个字母dd
# a = "aAsmr3idd4bgs7Dlsf9eAF"
# l = list(a)
# l.remove(a[0])
# l.remove(a[-1])
# index = l.index("d")
# l.remove(l[index])
# l.remove(l[index])
# print("".join(l))


# 159、“ksljj!@kkk122$ (sfsf*kjk<12abd/kk}XYZ”，以字符串中所有相邻的字母整体为列表元素，生成一个列表?
# s = "ksljj!@kkk122$ (sfsf*kjk<12abd/kk}XYZ"
# result = []
# for v in s:
#     if not v.isalpha():
#         s = s.replace(v, " ")
# temp_list = s.split()
# print(temp_list)


# 160、构造一个字典，key为9, 7, 5, 3, 1，value为一个包含两位小数的浮点数，且返回所有key、value项的和；
# round(1.2222)
# import random
#
# d = {}
# result = 0.0
# for i in range(9, 0, -2):
#     d[i] = round(random.uniform(1, 10), 2)
# for k, v in d.items():
#     result += (k + v)
# print("和: ", result)

# 161、求10000以内所有是素数且是闰年的数的和?
# import math
#
#
# def is_prime(num):
#     if num == 1:
#         return False
#     if num == 2:
#         return True
#     else:
#         for i in range(2, int(math.sqrt(num)) + 1):
#             if num % i == 0:
#                 return False
#         return True
#
#
# def is_leap_year(year):
#     if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#         return True
#     else:
#         return False
#
#
# result = 0
# for num in range(1, 10000):
#     if is_prime(num) and is_leap_year(num):
#         result += num
# print("和: ", result)

# 162、定义一个函数，形参包含字典参数、默认参数，返回所有传入参数组成字符串；
# def func(p1, p2="huhongqiang", **kwargs):
#     result = ""
#     result += str(p1)
#     result += p2
#     for k, v in kwargs.items():
#         result += str(k)
#         result += str(v)
#     return result
#
#
# d = {"name": "zhangsan", "age": 20}
#
# print(func("abc", **d))


# 163、一个字典key是人名、value是年龄，找出其中年龄最大的人
# d = {"张三": 25, "李四": 30, "王五": 80}
# for k, v in d.items():
#     if v == max(d.values()):
#         print("%s年龄最大" % k)


# 164、定义函数，用户输入n个字符串，输出排好序的字符串
# def sort_str(n):
#     result = []
#     for i in range(n):
#         s = input("请输入字符串")
#         sorted_s = "".join(sorted(list(s)))
#         result.append(sorted_s)
#     return result
#
#
# print(sort_str(3))

# 165、一个列表的元素均是字符串，求其中长度最小的字符串
# l = ["huhogniang","name","sex","abc"]
# min_length = len(l[0])
# result = []
# for value in l:
#     if len(value) < min_length:
#         min_length = len(value)
# for value in l:
#     if len(value) == min_length:
#         result.append(value)
# print("长度最小的字符串:",result)
