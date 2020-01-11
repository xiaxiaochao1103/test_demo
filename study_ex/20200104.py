#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os


# 习题1：定义一个类，实现读文件、写文件的方法


# class FileOperations(object):
#     def __init__(self, filepath):
#         self.filepath = filepath
#
#     def read_file(self):
#         try:
#             with open(self.filepath, "r", encoding="utf-8") as fp_obj:
#                 content = fp_obj.read()
#         except Exception as e:
#             print(e)
#         else:
#             return content
#
#     def write_file(self, content):
#         try:
#             with open(self.filepath, "w", encoding="utf-8") as fp_obj:
#                 fp_obj.write(content)
#         except Exception as e:
#             print(e)


# 习题2：定义一个类：实现功能可以返回随机的10个数字，随机的10个字母，随机的10个字母和数字的组合；字母和数字的范围可以指定；
# import random
#
#
# class RandomCombination(object):
#
#     def __init__(self, digit, letter):
#         self.digit = digit
#         self.letter = letter
#
#     def generate_random_numbers(self, n):
#         digit = ""
#         for i in range(n):
#             digit += random.choice(self.digit)
#         return digit
#
#     def generate_random_letters(self, n):
#         alphanum = ""
#         for i in range(n):
#             alphanum += random.choice(self.digit + self.letter)
#         return alphanum


# 习题3：找出一个文件中长度最长的10个单词
# import string
#
# with open("/Users/xiaxiaochao/PycharmProjects/untitled4/ssss/sssssssss.txt", "r", encoding="utf-8") as fp_obj:
#     content = fp_obj.read()
# for i in content:
#     if i in string.punctuation:
#         content = content.replace(i, " ")
# res = sorted(content.split(), key=len, reverse=True)[:10]
# print(res)
#
# import re
#
# with open("/Users/xiaxiaochao/PycharmProjects/untitled4/ssss/sssssssss.txt", "r") as file_obj:
#     content = file_obj.read()
# m = re.findall(r"\b[A-Za-z]+\b", content)
# res = sorted(m, key=len, reverse=True)[:10]
# print(res)


# 习题4:遍历字典的value值
#
# class Foo(object):
#     def __init__(self, d):
#         self.d = d
#
#     def __iter__(self):
#         return iter(self.d.values())  # 此处是求字典所有value的迭代器
#
#
# d = {1: "a", 2: "b"}
# f = Foo(d)
# for i in f:
#     print(i)


# 习题5:利用装饰器，写入文件并读取文件
def writefile(func):
    def _writefile(*args, **kwargs):
        with open("/Users/xiaxiaochao/PycharmProjects/untitled4/ssss/sssssssss.txt", "w") as file_obj:
            file_obj.write("x")
        func(*args, **kwargs)
    return _writefile

@writefile
def readfile(file_path):
    with open(file_path, "r") as file_obj:
        content = file_obj.read()
        print(content)


readfile("/Users/xiaxiaochao/PycharmProjects/untitled4/ssss/sssssssss.txt")
