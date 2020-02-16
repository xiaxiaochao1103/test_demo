#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 166、找出一个字符串中，重复出现的字母和出现次数
# s = "aabbcccddgk"
# data = {}
#
# for i in s:
#     if s.count(i) > 1:
#         data[i] = s.count(i)
#
# print(data)


# 167、删除字符串中的重复字符（重复字符只保留一个）?
# s = "aabbcccddgk"
# s = list(s)
# res = []
# for i in s:
#     if i not in res:
#         res.append(i)
#
# print("".join(res))


# 168、定义一个函数，形参定义为可变参数，返回所有传入参数的数字和；用户键盘输入一个整数n,随机生成n个三位数，利用定义的函数求随机生成的n个数字的和（提示：利用解包）
# import random
#
#
# def sum_iterable(*args, **kwargs):
#     res = 0
#     for i in args:
#         if isinstance(i, (int, float)):
#             res += i
#     for k, v in kwargs.items():
#         if isinstance(k, (int, float)):
#             res += k
#         if isinstance(v, (int, float)):
#             res += v
#     return res
#
#
# n = int(input("请输入数字个数: "))
# lis = [random.randint(1, 100) for i in range(n)]
# print(lis)
# print(sum_iterable(*lis))


# 169、生成一个文件，文件的每行内容是一个qq邮箱，邮箱长度自定义，文件行数自定义，邮箱名满足变量定义规则；
# import random
# import string
#
# with open("email.txt", "w", encoding="utf-8") as file_obj:
#     for i in range(10):
#         letters = string.ascii_letters + string.digits + "_"
#         letters_list = list(string.ascii_letters + string.digits + "_")
#         random.shuffle(letters_list)
#         first_email_name = random.choice(string.ascii_letters + "_")
#         other_email_name = "".join(random.sample(letters_list, 8))
#         email_name = first_email_name + other_email_name + "@qq.com"
#         file_obj.write(email_name + "\n")
#
# with open("email.txt", "r", encoding="utf-8") as file_obj:
#     for line in file_obj:
#         print(line)

# 170、两个字典的key,value交叉互换，一个字典的key，value 作为另一个字典的value，key。
# 比如：d1 = {"a":1,"b":2} d2= {"x":3,"y"：4} 编程实现 d1 ={3:"x",4:"y" } d2={1:"a",2:"b"}
# d1 = {"a": 1, "b": 2}
# d2 = {"x": 3, "y": 4}
# temp_d1 = {}
# temp_d2 = {}
# for k, v in d1.items():
#     temp_d2[v] = k
#
# for k, v in d2.items():
#     temp_d1[v] = k
#
#
# print(temp_d1, temp_d2)


# 171、统计一个文件中每行字母、数字及其个数，结果写入另外一个文件的对应行中。文件自己构造
# with open("time.txt", encoding="utf-8") as file_obj:
#     for line in file_obj:
#         letter_number = 0
#         digit_number = 0
#         other_number = 0
#         for c in line:
#             if c.isalpha():
#                 letter_number += 1
#             elif c in "0123456789":
#                 digit_number += 1
#             else:
#                 other_number += 1
#         with open("d:\\time_hhq.txt", "a", encoding="utf-8") as fp:
#             fp.write("数字个数:%d" % digit_number + " ")
#             fp.write("字母个数:%d" % letter_number + "  ")
#             fp.write("其他字符个数:%d" % other_number + "\n")
# with open("d:\\time_hhq.txt", encoding="utf-8")  as file_obj:
#     for line in file_obj:
#         print(line)


# 172、文件内容：
#
#  1class Student(object):
#  2   '''一个学生的类'''
#  3   __student_num =0
#  4   def __init__(self,name,school,grade,course=[],course_grade={}):
#  5      self.__name = name
#  6        self.school = school
#  7       self.grade =grade
#  8        self.course = course
#  9        self.course_grade = course_grade
# 10        Student.__student_num+=1
# 11p = Student()
# 把可运行代码取出存到一个文件中，去掉行号；
# with open("copy.txt", encoding="utf-8") as file_obj:
#     for line in file_obj:
#         with open("copy_2.txt", "a", encoding="utf-8") as fp:
#             fp.write(line[3:])
# with open("copy_2.txt", encoding="utf-8") as file_obj:
#     for line in file_obj:
#         print(line)


# 174、 计算 2  - 3  +  4  ‐  5  +  6  ... 前n项的和，n由键盘输入，用for 和while循环实现
# n = int(input("请输入个数："))
# res = 0
# for i in range(1, n+1):
#     if i % 2 == 1:
#         res += i + 1
#     elif i % 2 == 0:
#         res -= (i + 1)
#
# print(res)


# 175、输出banana对应的颜色，且输出其上层key（fruit）对应的value
# d = {
#     "info": {
#         "name": "zhangsan",
#         "age": 22,
#         "fruit": {
#             "peach": "red",
#             "banana": "yellow"
#         }
#     }
# }
#
#
# def xx(para, aims, res=[]):
#     for k, v in para.items():
#         print(k)
#         if k == aims:
#             res.append(v)
#             res.append(para)
#         else:
#             if isinstance(v, dict):
#                 xx(v, aims)
#     return res
#
#
# print(xx(d, "banana"))


# 176、使用匿名函数求100以内偶数的和
# print(sum(filter(lambda x: x % 2 == 0, list(range(10)))))


# 177、自己构造一个以字符串为key，数字为value的字典，分别按照key和value，倒序排序
# data = {"afj": 11, "ggs": 32, "dahd": 2, "bca": 97}
# print(sorted(data.items(), key=lambda x: x[0], reverse=True))
# print(sorted(data.items(), key=lambda x: x[1], reverse=True))


# 178、1+2!+3!+4!+5! 非递归实现求和
# result = 0
# temp = 1
# for num in range(1, 5 + 1):
#     temp *= num
#     result += temp
#     print(temp, result)
# print("和：", result)


# 179、给定一个字符串，判断其中的所有字符是不是都只出现一次；
# def is_one_time(s):
#     if s == "" or not isinstance(s, str):
#         return -1
#     for v in s:
#         if s.count(v) != 1:
#             return False
#     return True
#
#
# print(is_one_time("sda"))
# print(is_one_time("sdass"))


# 180、给定一个字符串，求该字符串的统计字符串。例如：“fffjkk99999022” ，返回统计字符串“f_3_j_1_k_2_9_5_0_1_2_2
# s = "fffjkk99999022"
# data = {}
# res = []
# for i in s:
#     data[i] = data.get(i, 0) + 1
#
# for k, v in data.items():
#     res.append(k)
#     res.append(str(v))
#
# print("_".join(res))


# 181、值传递和引用传递有什么区别？分别用值传递和引用传递实现一个函数；


# 184、比如[1,3,5,7,8,25,4,20]  25前面的总和为24，25后面的总和也是24，25这个点就是平衡点；
# 假如一个数组中的元素，其前面的部分等于后面的部分，那么这个点的位序就是平衡点?写程序实现，给定任何一个列表，找到它的所有平衡点和对应索引位置
# def finding_balance(para):
#     data = {}
#     for i in para:
#         if sum(para[:i]) == sum(para[i + 1:]):
#             print(i)
#             print(para[i])
#             data[para[i]] = i
#     return data
#
#
# print(finding_balance([1, 3, 5, 7, 8, 25, 4, 20]))


# 185、列表中某个元素出现的次数大于数组总数的一半时就成为支配数，其所在位序称为支配点；
# 比如[3,3,1,2,3]   3为支配数，0，1，4分别为支配点；?实现返回支配数和支配点
# def find_dominant_point(para):
#     result_items = []
#     for v in para:
#         if para.count(v) > len(para) // 2:
#             result_items.append(v)
#     result_items_index = []
#
#     for i in range(len(para)):
#         if para[i] in result_items:
#             result_items_index.append(i)
#     return result_items, result_items_index
#
#
# l = [3, 3, 1, 2, 3]
# print(find_dominant_point(l))


# 186、需求：启动程序后让用户输入工资，然后打印商品列表.允许用户根据商品编号购买商品.
# 用户选择商品后，检测余额是否足够，够就直接扣款，不够就提醒.
# 用户可一直购买商品，也可以随时退出，退出时，打印已经购买的商品和余额.例如：商品列表和商品价格如下，也可以自己构造原始数据;
# c_list = {"C001": "book", "C002": "phone", "C003": "milk"}
#
# pric_dict = {"C001": 4, "C002": 100, "C003": 8}
#
# buy_product_dict = {}
# salary = int(input("请输入工资: "))
# balance = salary
# end_flag = 0
# print("商品信息:")
# for k, v in c_list.items():
#     print(k, v, sep=":")
#
# print("商品价格信息:")
# for k, v in pric_dict.items():
#     print(k, v, sep=":")
#
# while True:
#     command = input("请输入你要选择的商品编号,输入q退出选择: ")
#     if command.lower() == "q":
#         print("购买的商品列表:", buy_product_dict)
#         print("余额:", balance)
#         break
#     else:
#         if command not in c_list.keys():
#             print("商品编号不存在，请重新输入")
#             continue
#     for product_num, product_name in c_list.items():
#         if command == product_num:
#             if balance >= pric_dict[product_num]:
#                 balance -= pric_dict[product_num]
#                 if product_num not in buy_product_dict:
#                     buy_product_dict[product_num] = 1
#                 else:
#                     buy_product_dict[product_num] += 1
#             else:
#                 print("余额不足!")
#                 end_flag = 1
#                 break
#     if end_flag:
#         break


