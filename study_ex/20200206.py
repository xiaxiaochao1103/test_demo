#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 231、按照阶乘思想，新建多层目录和文件，规则如下：
# 输入5，则会生成5级目录，根目录名称为”5的阶乘”，二级目录为5的阶乘的值为120，三级目录为4的阶乘为24....，五级目录为2的阶乘为2，然后其下文件为1.txt
# import os
#
#
# def factorial_list(n):
#     res = []
#     z = 1
#     for i in range(1, n + 1):
#         z *= i
#         res.append(z)
#     return res
#
#
# input_num = int(input("请输入一个数字："))
# f_list = factorial_list(input_num)
# path = str(input_num) + "的阶乘"
# if not os.path.exists(path):
#     os.mkdir(path)
#     os.chdir(path)
# if len(f_list) > 1:
#     for j in f_list[::-1]:
#         if j == 1:
#             with open(str(j) + ".txt", "w") as file_obj:
#                 pass
#         else:
#             os.mkdir(str(j))
#             os.chdir(str(j))
# else:
#     with open("1.txt", "w") as file_obj:
#         pass


# 232、文件升级操作，在e盘下先手动新建如下目录和文件，然后控制台接收输入1，则文件上升1级，
# 即a.txt就不在五级目录下了，而是跑到四级目录下面，输入4，则a.txt就在一级目录下面，输入5，则a.txt就在根目录下面
# import os
#
# print(os.path.sep)
# root = os.getcwd()
# path = root + "/一级目录/二级目录/三级目录/四级目录/五级目录"
#
# os.chdir(path)
# if os.path.exists("a.txt"):
#     os.remove("a.txt")
#
# n = int(input("请输入需要升级的级数: "))
# up_path = path.split(os.path.sep)
# print(up_path)
# if n < 5:
#     up_path = os.path.sep.join(up_path[:-n])
# elif n == 5:
#     up_path = "root"
# print(up_path)
# os.chdir(up_path)
# with open("a.txt", "w") as file_obj:
#     pass


# 233、同时读写文件，将文件内容为”i am learning gloryroad”读取出来后重新写入到该文件中，效果为按空格分割，每个单词均换行
# 即：文件内容为：”i am learning gloryroad”，读写文件后，就会变成如下效果：
# i
# am
# learning
# gloryroad
#
# with open("1.txt", "r+", encoding="utf-8") as fp_pbj:
#     content = fp_pbj.read()
#     content_list = content.split()
#     fp_pbj.seek(0, 0)
#     content_list = [i+"\n" for i in content_list]
#     fp_pbj.writelines(content_list)


# 234、统计你的e盘下有多少个文件扩展名为txt的文件，将统计的数目和找到的txt文件(全路径如”e:\\test\\a.txt”)打印出来
# import os
# count = 0
# for root, dirnames, files in os.walk("/Users/xiaxiaochao/PycharmProjects/test_demo/"):
#     for file in files:
#         if file[-4:] == ".txt":
#             count += 1
#             print(os.path.join(root, file))
#
#
# print(count)


# 235、找出文件中连续字母并重新写入该文件中，要求至少连续2位，反向连续不算(如ba)
# 如文件内容为”testabcedfcde”，则程序执行后打开该文件的内容应为：”ab cde”
# with open("1.txt", "r", encoding="utf-8") as fp_pbj:
#     content = fp_pbj.read()
#     print(content)
#     n = 0
#     res = []
#     while n < len(content) - 2:
#         start_index = n
#         while ord(content[n+1]) == ord(content[n]) + 1:
#             n += 1
#         end_index = n
#         print(start_index, end_index)
#         if end_index > start_index:
#             res.append(content[start_index:end_index+1])
#         else:
#             n += 1
#
# with open("1.txt", "w", encoding="utf-8") as fp_pbj:
#     print(res)
#     fp_pbj.write(" ".join(res))


# 236、写一个函数，生成随机的一个字符串，可以指定位数
# import random
# import string
#
#
# def random_str(n):
#     s = random.sample(string.ascii_letters+string.digits, n)
#     return "".join(s)
#
#
# print(random_str(5))


# 237、获取两个字符串中最大相同子串
# s1 = "1abcdefghijk"
# s2 = "22abcd12"
# s = []
# for i in range(len(s2)):
#     for j in range(len(s2) - i):  # 每次循环后续字符串变短
#         s.append(s2[i:i + j + 1])
# print(s)
# result = []
# for sub in s:
#     if sub in s1:
#         result.append(sub)
# print(result)
# print("最长的子串:", sorted(result, key=len)[-1])


# 238、列出一个字符串中包含某个子字符串的所有坐标
# def find_str_index(s, sub):
#     res = []
#     for i in range(len(s)):
#         if s[i: i+len(sub)] == sub:
#             res.append(i)
#     return res
#
#
# print(find_str_index("dadahadaksjda", "da"))


# 239、请将a字符串的所有数字取出，并输出成一个新的纯数字字符串
# def find_num(a):
#     res = []
#     for i in a:
#         if i.isdigit():
#             res.append(i)
#     return "".join(res)
#
#
# print(find_num("2g2g4g4jg232343g3232jb42"))

# 240、请去除a字符串多次出现的字母，仅留最先出现的一个，且字母顺序保持不变。例 ‘abcabb’，经过去除后，输出 ‘abc’
# def deduplication_str(a):
#     res = ""
#     for i in a:
#         if i not in res:
#             res += i
#     return res
#
#
# print(deduplication_str("abcabb"))