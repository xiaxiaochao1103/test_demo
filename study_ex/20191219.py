#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 6. 命题练习:
# 1） 一个目录下只有文件（自己构造），拷贝几个文件（手工完成）
# 2 ）用listdir函数获取所有文件，如果文件的创建时间是今天，那么就在文件里面写上文件的路径、
# 文件名和文件扩展名
# 3） 如果不是今天创建（获取文件的创建时间，并转化为时间格式，判断是否今天），请删除
# 4 ）计算一下这个程序的执行耗时
import os

# import time
# start_time = time.time()
# os.chdir("/Users/xiaxiaochao/PycharmProjects/untitled4/ssss")
# lis_file = os.listdir()
# for file in lis_file:
#     if time.strftime("%Y-%m-%d") == time.strftime("%Y-%m-%d",time.localtime(os.path.getctime(file))):
#         with open(file, "w", encoding="utf-8") as file_obj:
#             file_obj.write(os.path.abspath(file))
#     else:
#         os.remove(file)
# end_time = time.time()
# print(end_time - start_time)


# 7.删除某个目录下的全部文件
# os.chdir("/Users/xiaxiaochao/PycharmProjects/untitled4/ssss")
# lis_file = os.listdir()
# for file in lis_file:
#     if os.path.isfile(file):
#         os.remove(file)


# 8.统计某个目录下文件数和目录个数
# count_file = 0
# count_dir = 0
# os.chdir("/Users/xiaxiaochao/PycharmProjects/untitled4/ssss")
# lis_file = os.listdir()
# for file in lis_file:
#     if os.path.isfile(file):
#         count_file += 1
#     else:
#         count_dir += 1
# print(count_file, count_dir)


# 9.删除某个目录下的全部文件(仅限一级目录)
# 遍历所有的目录、文件，如果主目录等于一级目录，删除其下的文件
# for root, dirs, files in os.walk("/Users/xiaxiaochao/PycharmProjects/untitled4/ssss"):
#     if root == "/Users/xiaxiaochao/PycharmProjects/untitled4/ssss":
#         for path in os.listdir(root):
#             os.chdir(root)
#             if os.path.isfile(path):
#                 os.remove(path)


# 10.使用程序建立一个多级的目录，在每个目录下，新建一个和目录名字一样的txt文件
# import os
# os.chdir("/Users/xiaxiaochao/PycharmProjects/untitled4/ssss")
# for i in range(3):
#     os.mkdir(str(i))
#     os.chdir(str(i))
#     with open(str(i)+".txt", "w", encoding="utf8") as file_obj:
#         pass


# 11.查找某个目录下是否存在某个文件名
def find_file(dir_path, file):
    os.chdir(dir_path)
    return os.path.exists(file)


print(find_file("/Users/xiaxiaochao/PycharmProjects/untitled4/ssss", "1.txt"))


# 12.用系统命令拷贝文件
os.system("cp /home/1.txt /root/1.txt")