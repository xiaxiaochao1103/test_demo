#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 文件访问访问一存在多行的文件，实现每隔一秒逐行显示文本内容的程序，
# 每次显示文本文件的 5行, 暂停并向用户提示“输入任意字符继续”，按回车键后继续执行，直到文件末尾。
# import time
# with open("/Users/xiaxiaochao/PycharmProjects/untitled4/ssss/ssder.txt", "r", encoding="utf-8") as file:
#     contents = file.readlines()
#     for i in range(len(contents)):
#         print(contents[i])
#         time.sleep(1)
#         if i == 4:
#             command = input("输入任意字符继续")
#             if command is not None:
#                 continue
#             else:
#                 break


# 同时读写文件
# with open("/Users/xiaxiaochao/PycharmProjects/untitled4/ssss/sssssssss.txt",encoding="utf8") as file_obj:
#     for line in file_obj:
#         with open("/Users/xiaxiaochao/PycharmProjects/untitled4/ssss/zzz.txt","a",encoding="utf8") as file_obj2:
#             file_obj2.write(line)

# 23、创建一个空文件
# with open("/Users/xiaxiaochao/PycharmProjects/untitled4/ssss/sssssssss.txt", "w", encoding="utf-8") as file:
#     pass

# 24、读取文件的前两行
# with open("/Users/xiaxiaochao/PycharmProjects/untitled4/ssss/ssder.txt", "r", encoding="utf-8") as file:
#     print(file.readline())
#     print(file.readline())


# 25、读取文件的奇数行
# with open("/Users/xiaxiaochao/PycharmProjects/untitled4/ssss/ssder.txt", "r", encoding="utf-8") as file:
#     contents = file.readlines()
#     for i in range(len(contents)):
#         if i % 2 == 1:
#             print(contents[i])


# 在文件中写入一个列表的内容
# lines = ["1\n", "2\n", "3\n"]
# with open("/Users/xiaxiaochao/PycharmProjects/untitled4/ssss/ssddder.txt", "w", encoding="utf-8") as file:
#     file.writelines(lines)

# 27、在文件中的0、2、4位置写入当前的文件位置偏移量
# with open("/Users/xiaxiaochao/PycharmProjects/untitled4/ssss/ssder.txt", "w", encoding="utf8") as file_obj:
#     file_obj.write(str(file_obj.tell()))
#     file_obj.seek(2, 0)
#     file_obj.write(str(file_obj.tell()))
#     file_obj.seek(4, 0)
#     print(file_obj.write(str(file_obj.tell())))


# 28、with写法读取文件内容
# with open("/Users/xiaxiaochao/PycharmProjects/untitled4/ssss/ssder.txt", encoding="utf8") as file_obj:
#     lines = file_obj.readlines()
#     print(lines)


# 29、统计一个文件中单词的个数
# 文件内容：
# glory road ,wu lao shi
# file,haha
# women, man, love文件内容：
# glory road ,wu lao shi
# file,haha
# women, man, love
# import string
# with open("/Users/xiaxiaochao/PycharmProjects/untitled4/ssss/sssssssss.txt", encoding="utf8") as file_obj:
#     contents = file_obj.read()
#
#
# for i in contents:
#     if i in string.punctuation:
#         contents = contents.replace(i, " ")
#
# print(len(contents.split()), contents.split())


# 将一个文件的所有单词倒序写入文件中
import string
with open("/Users/xiaxiaochao/PycharmProjects/untitled4/ssss/sssssssss.txt", encoding="utf8") as file_obj:
    contents = file_obj.read()

with open("/Users/xiaxiaochao/PycharmProjects/untitled4/ssss/sssssssss.txt", "w", encoding="utf8") as file_obj:
    for i in contents:
        if i in string.punctuation:
            contents = contents.replace(i, " ")
    file_obj.writelines("".join(contents.split()[::-1]))