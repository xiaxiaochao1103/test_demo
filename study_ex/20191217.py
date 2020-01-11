#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 习题13:在当前目录下，找到1小时内新建的所有文件。
# 算法：
# 取出某个目录内，1小时内新建的所有文件名。
# import os
# import time
#
# res = []
# os.chdir("/Users/xiaxiaochao/PycharmProjects/untitled4")
# for file in os.listdir():
#     if os.path.isfile(file):
#         print(os.stat(file).st_ctime, time.time())
#         if os.stat(file).st_ctime - time.time() < 3600:
#             res.append(file)
#
# print(res)

# 习题14:小练习，把所有的txt文件干掉。新建一个空的子目录xxx，放在某个层级下,把它删掉
# import os
# for root, dirs, files in os.walk("/Users/xiaxiaochao/PycharmProjects/untitled4/ssss"):
#     os.chdir(root)
#     print(files, dirs)
#     for file in files:
#         print(file)
#         if file[-4:] == '.txt':
#             os.remove(file)
#     for dir in dirs:
#         if dir == "xxx":
#             os.rmdir(dir)


# 习题15:统计一个文件夹下所有文件类型
# import os
# data = {}
# for root, dirs, files in os.walk("/Users/xiaxiaochao/PycharmProjects/untitled4/ssss"):
#     os.chdir(root)
#     print(files, dirs)
#     for file in files:
#         post_name = os.path.splitext(file)
#         data[post_name[1]] = data.get(post_name, 0) + 1
#
# print(len(data))
#
#
# # 1.基础题：
# # 检验给出的路径是否是一个文件：
# # 检验给出的路径是否是一个目录：
# # 判断是否是绝对路径：
# # 检验给出的路径是否真地存:
# import os
#
# print(os.path.isfile("/Users/xiaxiaochao/PycharmProjects/untitled4/ssss/ss.txt"))
# print(os.path.isdir("/Users/xiaxiaochao/PycharmProjects/untitled4/ssss"))
# print(os.path.isabs("/Users/xiaxiaochao/PycharmProjects/untitled4/ssss"))
# print(os.path.exists("/Users/xiaxiaochao/PycharmProjects/untitled4/ssss"))
#
# # 2.返回一个路径的目录名和文件名
#
# print(os.path.dirname("/Users/xiaxiaochao/PycharmProjects/untitled4/ssss/ss.txt"))
# print(os.path.basename("/Users/xiaxiaochao/PycharmProjects/untitled4/ssss/ss.txt"))
# print(os.path.split("/Users/xiaxiaochao/PycharmProjects/untitled4/ssss/ss.txt"))
#
# # 3.分离文件名与扩展名
# print(os.path.splitext("/Users/xiaxiaochao/PycharmProjects/untitled4/ssss/ss.txt"))
#
# # 4.找出某个目录下所有的文件，并在每个文件中写入“gloryroad”
# import os
#
# os.chdir("/Users/xiaxiaochao/PycharmProjects/untitled4/ssss")
# list_dir = os.listdir()
# for file in list_dir:
#     if os.path.isfile(file):
#         with open(file, "r+", encoding="utf-8") as file_obj:
#             file_obj.write("gloryroad")
#
# # 5.如果某个目录下文件名包含txt后缀名，则把文件后面追加写一行“被我找到了！”
# import os
#
# os.chdir("/Users/xiaxiaochao/PycharmProjects/untitled4/ssss")
# list_dir = os.listdir()
# for file in list_dir:
#     if os.path.isfile(file):
#         if ".txt" in file:
#             with open(file, "r+", encoding="utf-8") as file_obj:
#                 file_obj.read()
#                 file_obj.write("被我找到了")
