#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 51、写函数，计算传入字符串中【数字】、【字母】、【空格] 以及 【其他】的个数
# def count_letter(string):
#     digit_count = 0
#     letter_count = 0
#     space_count = 0
#     other_count = 0
#     for i in string:
#         if i.isdigit():
#             digit_count += 1
#         elif i.isalpha():
#             letter_count += 1
#         elif i.isspace():
#             space_count += 1
#         else:
#             other_count += 1
#     return digit_count, letter_count, space_count, other_count
#
#
# print(count_letter("12adf!@#    456"))


# 52、写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。
# def count_length(para):
#     if not isinstance(para, (str, list, tuple)):
#         print("传入参数类型错误")
#         return
#     else:
#         if len(para) > 5:
#             return True
#         else:
#             return False
#
#
# print(count_length("adbddd"))
# print(count_length(["a", "b", "c"]))
# print(count_length((1, 2, 3, 4, 5, 5)))
# print(count_length({1, 2}))


# 53、写函数，检查用户传入的对象（字符串、列表、元组）的每一个元素是否含有空内容。
# def check_space(para):
#     if not isinstance(para, (str, list, tuple)):
#         print("传入参数类型错误")
#         return
#     else:
#         flag = False
#         for i in para:
#             if i == " ":
#                 flag = True
#         return flag
#
#
# print(check_space("adbddd "))
# print(check_space(["a", "b", "c", " "]))
# print(check_space((1, 2, 3, 4, " ", 5)))
# print(check_space({1, 2}))


# 54、写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
# def check_length(para):
#     if not isinstance(para, list):
#         print("传入参数类型错误")
#         return
#     else:
#         if len(para) > 2:
#             return para[:2]
#         else:
#             return para
#
#
# print(check_length("adbddd "))
# print(check_length(["a", "b", "c", " "]))
# print(check_length([1, 2]))


# 55、写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。
# def odd_element(para):
#     if not isinstance(para, (list, tuple)):
#         print("传入参数类型错误")
#         return
#     else:
#         return para[1::2]
#
#
# print(odd_element([1, "a", 2]))
# print(odd_element((1, 1, 2, 3)))
# print(odd_element([1]))
# print(odd_element([]))


# 56、写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
# def value_element(para):
#     if not isinstance(para, dict):
#         print("传入参数类型错误")
#     else:
#         for key, value in para.items():
#             if isinstance(value, (str, list, tuple)):
#                 para[key] = value[:2]
#             elif isinstance(value, int):
#                 para[key] = int(str(value)[:2])
#             elif isinstance(value, set):
#                 para[key] = set(list(value)[:2])
#     return para
#
#
# d = {"a": {1, 2, 3, 4}, "b": "xyzccc", "c": 123456}
# d1 = {"a": {1}, "b": "x", "c": 1}
# print(value_element(d))
# print(value_element(d1))


# 57、写函数，利用递归获取斐波那契数列中的第 10 个数，并将该值返回给调用者。
# def fib(num):
#     if num == 1 or num == 2:
#         return 1
#     else:
#         return fib(num - 1) + fib(num - 2)
#
#
# print(fib(10))


# 58、写函数，，用户传入修改的文件名，与要修改的内容，执行函数，完成整个文件的批量修改操作
# def modify_file(file_name, source, dest):
#     with open(file_name, "r+") as file_obj:
#         content = file_obj.read()
#         file_obj.seek(0, 0)
#         file_obj.write(content.replace(source, dest))
#
#
# modify_file("a.txt", "post", "put")


# 59、别后续的字符串："bat","bit","but","hat","hit","hut"
# import re
#
# res = [re.match(r"[bh][aiu]t", i).group() for i in ["bat", "bit", "but", "hat", "hit", "hut"]]
# print(res)


# 60、匹配由单个空格分隔的任意单词对，也就是姓 和名
# import re
# re.search(r"[a-zA-Z]+\s[a-zA-Z]+]", "da sss").group()


# 61、匹配由单个逗号和单个空白符分隔的任何单词和单个字母，如姓氏的首字母
# import re
# print(re.search(r",\s(([a-z])[a-z]+)", "dad, dasj").group(1))
# print(re.search(r",\s(([a-z])[a-z]+)", "dad, dasj").group(2))


# 62、匹配所有有效Python标识符的集合
# import re
#
# print(re.search(r"^[a-z|_]\w+", "_ad32", re.I).group())
# print(re.search(r"^[a-z|_]\w+", "aa_ad32", re.I).group())
# print(re.search(r"^[a-z|_]\w+", "Aa_ad32", re.I).group())
# print(re.search(r"^[a-z|_]\w+", "11_ad32", re.I).group())


# 63、匹配街道地址（使你的正则表达式足够通用，来匹配任意数量的街道单词，包括类型名称）例如，美国街道地址使用如下格式：1180 Bordeaux Drive。
# 使你的正则表达式足够灵活，以支持多单词的街道名称，如3120 De la Cruz Boulevard
# import re
#
# print(re.search(r"([0-9a-zA-Z]+\s?)+", "3120 De la Cruz Boulevard").group())
# print(re.search(r"([0-9a-zA-Z]+\s?)+", "1180 Bordeaux Drive").group())
# print(re.match(r"\d{4}(\s[a-z]+)+", "3120 De la Cruz Boulevard", re.I).group())
# print(re.match(r"\d{4}(\s[a-z]+)+", "1180 Bordeaux Drive", re.I).group())


# 64、匹配以"www"起始且以“.com”结尾的简单Web域名；例如，http://www.yahoo.com
# 选做题：你的正则表达式也可以支持其他高级域名，如.edu,.net等（例如，http://www.foothill.edu）
# import re
# res = re.findall(r"http://((\w+.)+[com|edu])", "http://www.yahoo.com")
# print(res[0][0])
# res = re.findall(r"http://((\w+.)+[com|edu])", "http://www.foothill.edu")
# print(res[0][0])


# 65、匹配所有能表示Python整数的字符串集
# import re
#
# print(re.search(r"-?[1-9]\d*|0", "10").group())
# print(re.search(r"-?[1-9]\d*|0", "-4").group())
# print(re.search(r"-?[1-9]\d*|0", "0").group())


# 66、匹配所有能表示Python浮点数的字符串集
# import re
#
# print(re.search(r"-?([1-9]\d*|0)\.\d+", "10.1").group())
# print(re.search(r"-?([1-9]\d*|0)\.\d+", "-4.566").group())
# print(re.search(r"-?([1-9]\d*|0)\.\d+", "-0.02").group())


# 67、匹配所有能表示复数的字符串集
# import re
#
# i = "10+20j"
# print(re.match(r"\d+\+\d+j",i).group())


# 68、匹配所有能表示有效电子邮件地址的集合（从一个宽松的正则表达式开始，然后尝试使它尽可能严谨，不过要保证正确的功能）
# import re
# print(re.search(r"\w+@\w+\.(com|edu|net)", "11@qq.com").group())


# 69、匹配所有能表示有效网站地址的集合（URL）（从一个宽松的正则表达式开始，然后尝试使它尽可能严谨，不过要保证正确的功能）
# import re
#
# print(re.search(r"http(s)?(://)(\w+\.)+(com|net|edu|org)", "https://www.baidu.com").group())


# 70、创建一个能从type()的结果中提取实际类型名称的正则表达式. ““”-返回int
# import re
#
#
# def get_type(para):
#     str_type = str(type(para))
#     res = re.findall(r"<class '([a-z]+)'>", str_type, re.I)[0]
#     return res
#
#
# def s():
#     pass
#
#
# class Ss(object):
#     pass
#
#
# print(get_type(1))
# print(get_type([]))
# print(get_type({}))
# print(get_type(()))
# print(get_type(s))
# print(get_type(Ss))


# 71、请写出一个正则表达式表示标准的日历上的其他三个月（十月、十一月、十二月）
# import re
# pattern = re.compile(r"1[0-2]")
# print(pattern.match("10").group())
# print(pattern.match("11").group())
# print(pattern.match("12").group())


# 72、写一个正则表达式，可以 用连字符分割信用卡号，比如：16位信用卡号格式是4-4-4-4，数位不足时填0补位


# 数据文件：d:\\redata.txt
# 以下73到83基于此数据文件
# Fri Apr 12 02:04:19 2030::mtdhaym@ogyiqsnkak.net::1902161059-7-10
# Sun Sep  2 14:33:07 1973::ombdal@sfbpvxkr.gov::115799587-6-8
# Wed Aug 21 05:11:12 2030::rpfdkth@vvjiktevwx.org::1913490672-7-10
# Sun Jan  6 08:14:19 1980::pequjh@paeqndq.gov::315965659-6-7
# Sat Mar 29 15:17:51 1975::cdpee@rujhfqppurg.net::165309471-5-11
# Wed Jul 22 19:47:29 1970::vxmlvj@olvqlcvwdoy.gov::17495249-6-11
# Thu May 12 08:08:08 2022::xwefmf@ckyoesgbwd.edu::1652314088-6-10
# Mon Jul 10 03:27:13 1978::xplwl@usaodfugeso.edu::268860433-5-11
# 73、统计生成的redata.txt文件中，星期中的每一天出现的次数
# import re
#
# data = {}
# with open("redata.txt", "r", encoding="utf-8") as fp_obj:
#     for line in fp_obj:
#         # data[line[:3]] = data.get(line[:3], 0) + 1
#         weekday = re.match(r"[A-Za-z]{3}", line).group()
#         data[weekday] = data.get(weekday, 0) + 1
# print(data)


# 74、通过检查每个输出行中整型字段部分的第一个整型是否和该行开头的时间戳相匹配来验证redata.txt中的数据知否完好
# # 匹配到时间戳 匹配到第一个整数，然后计算整数对应的时间是否是时间戳的值
# import time
# import re
#
# with open("redata.txt", "r") as file_obj:
#     for line in file_obj:
#         format_time = re.match(r"(.*?)::", line).group(1)
#         timestamp = float(re.search(r"::(\d+)", line).group(1))
#         if format_time != time.ctime(timestamp):
#             print(format_time)
#             print(time.ctime(timestamp))
#             print("the data file is not complete.")
#         else:
#             print("the data file is complete.")

# 75、提取每行中的完整时间戳字段
# import re
# res = []
# pattern = re.compile(r"(.*?)::")
# with open("redata.txt") as file_obj:
#     for line in file_obj:
#         res.append(pattern.match(line).group(1))
# print(res)


# 76、提取每行完整的电子邮件地址
# import re
#
# emails = []
# with open("redata.txt", "r", encoding="utf-8") as fp_obj:
#     contents = fp_obj.readlines()
#     for line in contents:
#         emails.append(re.findall("::(.*)::", line)[0])
# print(emails)


# 77、只提取时间戳字段中的月份
# import re
#
# pattern = re.compile(r"[A-Za-z]{3}\s([A-Za-z]{3})")
# res = []
# with open("redata.txt", "r", encoding="utf-8") as fp_obj:
#     for line in fp_obj:
#         res.append(pattern.search(line).group(1))
# print(res)


# 78、只提取时间戳字段中的年份
# import re
#
# pattern = re.compile(r"\s(\d{4})::")
# res = []
# with open("redata.txt", "r", encoding="utf-8") as fp_obj:
#     for line in fp_obj:
#         res.append(pattern.search(line).group(1))
# print(res)


# 79、只提取时间戳字段中的值（格式： HH: MM:SS）
# import re
#
# pattern = re.compile(r"\d{2}:\d{2}:\d{2}")
# res = []
# with open("redata.txt", "r", encoding="utf-8") as fp_obj:
#     for line in fp_obj:
#         res.append(pattern.search(line).group())
# print(res)


# 80、只从电子邮件地址中提取出登录名和域名（包括主域名和顶级域名，二者连在一起）
# import re
#
# pattern = re.compile(r"::([0-9a-z]+)@[a-z]+.([a-z]+)::", re.I)
# res = []
# with open("redata.txt", "r", encoding="utf-8") as fp_obj:
#     for line in fp_obj:
#         res.append(pattern.search(line).group(1) + ":" + pattern.search(line).group(2))
# print(res)


# 81、只从电子邮件地址中提取出登录名和域名（包括主域名和顶级域名，二者分别提取）
# import re
#
# pattern_login = re.compile(r"::([0-9a-z]+)@", re.I)
# pattern_domain = re.compile(r"\.([a-z]+)::", re.I)
# login = []
# domain = []
# with open("redata.txt", "r", encoding="utf-8") as fp_obj:
#     for line in fp_obj:
#         login.append(pattern_login.search(line).group(1))
#         domain.append(pattern_domain.search(line).group(1))
# print(login, "\n", domain)

# 82、将每行中的电子邮件地址替换为你自己的电子邮件地址
# import re
# with open("redata.txt") as file_obj:
#     for line in file_obj:
#         s = re.sub(r"\w+@\w+.\w+", "xxc@qq.com", line)
#         with open("redata_2.txt", "a") as file_obj2:
#             file_obj2.write(s)


# 83、提取出时间戳中的月、日、年，并按照格式“月日，年”显示出来，且每行仅遍历一次
# import re
# times = []
# pattern = re.compile(r"\w{3}\s(\w{3})\s{1,2}(\d{1,2}?).*?(\d{4})")
# with open("redata.txt") as file_obj:
#     for line in file_obj:
#         time = "%s %s,%s" % (pattern.search(line).group(1),
#                              pattern.search(line).group(2), pattern.search(line).group(3))
#         times.append(time)
# print(times)


# 84、匹配800 - 555 - 1212和555 - 1212，都可以匹配
# import re
# pattern = re.compile(r"(\d{3}-)?\d{3}-\d{4}")
# print(pattern.match("800-555-1212").group())
# print(pattern.match("555-1212").group())

# 85、同时可以匹配800 - 555 - 1212、555 - 1212和（800）-555 - 1212
# import re
# pattern = re.compile(r"(\(\d{3}\)-|\d{3}-)?\d{3}-\d{4}")
#
# print (pattern.match("800-555-1212").group())
# print (pattern.match("555-1212").group())
# print (pattern.match("(800)-555-1212").group())
