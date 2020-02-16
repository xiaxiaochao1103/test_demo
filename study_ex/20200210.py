#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 246、输入一个字符串，包含四种类型的字符，大写字母，小写字母，数字，减号（-）
# 要求： 对输入的字符串做相应的展开并且输出，如a-d展开为abcd，A-C展开为ABC，4-4展开成4
# def func(p):
#     s = []
#     result = []
#     for i in range(0, len(p), 3):
#         s.append(p[i:i + 3])
#     print(s)
#     for value in s:
#         temp = ""
#         if value[0] not in "0123456789":
#             for n in range(ord(value[0]), ord(value[-1]) + 1):
#                 temp += chr(n)
#
#         else:
#             temp = value[0]
#         result.append(temp)
#     return "".join(result)
#
#
# print(func("a-dA-C4-4"))


# 247、“1234”转换为一个数字，要求不使用内置函数
# s = "1234"
# num = 0
# s = s[::-1]
# for i,v in enumerate(s):
#     for j in range(10):
#         if v == str(j):
#             num += j*(10**i)
# print(num)


# 248、统计一个字符串只出现一次的所有字母，将这些字母拼成一个新串，并且按照字母第一次在字符串出现的位置排序，不允许使用count,
# # 方法一
# s = "sdfkjk122Adkjjkkkaabbee"
# data = {}
# res = []
# for i in s:
#     data[i] = data.get(i, 0) + 1
#
# for k, v in data.items():
#     if v == 1 and k.isalpha():
#         res.append(k)
#
# print("".join(res))
#
#
# # 方法二
# s = "sdfkjk122Adkjjkkkaabbee"
# s_dict = {}#存不重复字符及索引
# for i in range(len(s)):
#     if s[i] not in s[i+1:] and s[i] not in s[:i]and s[i].isalpha():
#         s_dict[s[i]] = s.index(s[i])
# print("不重复的字母:",s_dict)
# new_str = "".join(s_dict)
# print("生成的新串即是排序后的串:",new_str)


# 249、输入一个字符串，输出该字符串中对称的子字符串的最大长度。 比如输入字符串“google”，由于该字符串里最长的对称子字符串是“goog”，因此输出4。
# def sub_str_length(s):
#     sub_list = []
#     result_sub = []
#     for i in range(len(s)):
#         for j in range(len(s) - i):  # 每次循环后续字符串变短
#             sub_list.append(s[i:i + j + 1])
#
#     for sub in sub_list:
#         if sub == sub[::-1]:
#             result_sub.append(sub)
#
#     return len(sorted(result_sub, key=len)[-1])
#
#
# print(sub_str_length("agoogle"))


#  249、在TeX中，左双引号，右双引号是”。输入一篇包含双引号的文章，你的任务是把它转换成TeX格式。
# 样例输入：
# “To be or not to be,” quoth the Bard, “thatis the question”.
# 样例输出：
# To be or not to be,” quoth the Bard,that is the question”. （竞赛题）
# def convert_str(s):
#     n = 0
#     for v in s:
#         if v == '“':
#             s = s.replace('“', '``')
#     return s
#
#
# s = '“To be or not to be,” quoth the Bard, “thatis the question”.'
# print(convert_str(s))


# 250、16 如果一个字符串可以由某个长度为k的字符串重复多次得到，我们说该串以k为周期。
# 例如，abcabcabcabc以3为周期（注意，它也以6和12为周期）。输入一个长度不超过80的串，输出它的最小周期。 样例输入：HoHoHo 样例输出：2 （竞赛题）
# def ss(s):
#     sub_list = []
#     res = []
#     for i in range(len(s)):
#         for j in range(len(s) - 1):
#             sub_list.append(s[i:i + j + 1])
#     print(sub_list)
#     for i in sub_list:
#         n = 1
#         while len(i * n) <= len(s):
#             if i * n == s:
#                 res.append(i)
#             n += 1
#     return sorted(res, key=len)[0]
#
#
# print(ss("abcabcabcabc"))


# 251、”abcdefghi”，如果n = 2，移位后应该是”hiabcdefg”
# def offset(s, n):
#     if len(s) <= n:
#         return s
#     else:
#         return s[-n:] + s[:-n]
#
#
# s = "abcdefghi"
# print(offset(s, 4))


# 252、从键盘输入多个任意长度的单词，当输入“#”符时结束输入（字符串内容不包括“#”），然后程序反向输出所有输入的单词。
# ori_list = []
# while 1:
#     word = input(">>")
#     if word == "#":
#         break
#     ori_list.append(word)
# for word in ori_list[::-1]:
#     print(word)


# 253、如何确定一个纯ascii字符串中是否所有字符全部互不相同
# s = "sdfkjljkjlkjkl2323"
# s2 = "12abc"
#
#
# def if_all_diff(s):
#     for v in s:
#         if s.count(v) > 1:
#             return False
#     return True
#
#
# print(if_all_diff(s))
# print(if_all_diff(s2))


# 254、s = "ajldjlajfdljfddd"，去重并从小到大排序输出"adfjl"
# s = "ajldjlajfdljfddd"
# s = list(s)
# print("".join(sorted(list(set(s)))))

# 255、字符串a = "not 404 found 张三 99 深圳"，请取出所有中文部分
# import re
#
# a = "not 404 found 张三 99 深圳"
#
# result = []
# l = a.split()
# str_list = re.findall(r"\b[a-zA-Z]+\b", a)
# print(str_list)
# for value in l:
#     if value not in str_list and not value.isdigit():
#         result.append(value)
# print(result)
