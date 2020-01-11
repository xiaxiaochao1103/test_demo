#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 习题6:处理数据文件
# 数据文件：data.log
# 20160215000148|0|collect info job pos|success|
# 20160215000153|0|collect info job end|success|resultcode = 0000
# 20160216000120|0|collect info job pos|success|
# 20160216000121|0|collect info job end|success|resultcode = 0000
# 20160217000139|0|collect info job pos|success|
# 20160217000143|0|collect info job end|success|resultcode = 0000
#
#
# 数据分析需求：
# 每行内容需要生成以每行首年月日为名称的文件，文件内容写入|0|后的所有行内容（也包括|0| ）
# 算法分析：
# 遍历每一行，每行取头8个字母
# 新建文件，文件名为首8个字母，然后把第15字符后的所有字
# 符拷贝到文件中
# 关闭文件


with open("data.log", "r", encoding="utf-8") as file_obj:
    for line in file_obj:
        with open("data.log" + str(line[:14]) + ".txt", "w", encoding="utf-8") as file_obj2:
            file_obj2.write(line[14:])

# 习题7:删除一个目录下文件

# import os
# import  os.path
# os.chdir("e:\\python2")
# list1 = os.listdir("e:\\python2")
#
# for content in list1:
#     if os.path.isfile(content):
#         os.remove(content)


# 习题8：文件中有两行内容，在中间再加入一行
# with open("a.txt", "r", encoding="utf-8") as file:
#     content = file.readlines()
#     print(content)
#     content.insert(1, "----------\n")
# with open("a.txt", "w", encoding="utf-8") as file:
#     file.write("".join(content))


# 习题9:读一个文件，包含英文句子，请统计共多少个不重复的单词，#并且在另外一个文件中打印每个单词以及它的出线次数
import string
# words = ""
# words_dict = {}
# with open("b.txt", "r", encoding="utf-8") as file:
#     for line in file:
#         for j in line:
#             if not j.isalpha():
#                 line = line.replace(j, " ")
#         words += line
#     word_list = words.split()
#     print(word_list)
#     for i in word_list:
#         words_dict[i] = words_dict.get(i, 0) + 1
#
# with open("c.txt", "w", encoding="utf-8") as file:
#     for key, value in words_dict.items():
#         file.write("%s : %s\n" % (key, value))


# 习题10：写个记账程序，每天收入多少，支出多少，总额剩多少，使用序列化方式保存信息
import pickle

income = []
spend = []
deposit = 0.0

while 1:
    command = input("请输入收入、支出和金额，如: 支出>50,输入q退出: ")
    if command.lower() == "q":
        break
    try:
        amount = float(command.split(">")[1])
    except Exception as e:
        print("输入错误，请重新输入")
        continue
    else:
        type = command.split(">")[0]
        if type == "收入":
            income.append(amount)
            deposit += amount
        elif type == "支出":
            if deposit - abs(amount) >= 0:
                spend.append(abs(amount))
                deposit -= amount
            else:
                print("余额不足！")

print("收入:", income)
print("支出:", spend)
print("余额:", deposit)

file_obj = open("d.txt", "wb")

pickle.dump(income, file_obj)
pickle.dump(spend, file_obj)
pickle.dump(spend, file_obj)
file_obj.close()
