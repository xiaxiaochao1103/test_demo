#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 习题12：代码行统计工具
import os

"""	
1、根据命令行输入的统计目录及文件类型进行统计目录或单个文件的代码行数

"""


# 统计指定目录、指定文件类型文件的代码量
def count_all_file_code(count_path, file_types=None):
    # 判断传入的文件类型list是否为空，如果为空指定文件类型
    if len(file_types) == 0:
        file_types = [".py", ".cpp", ".java", ".c", ".h", ".php", ".asp"]

    # 存储所有文件总代码量
    total_line_number = 0
    # 存储每个文件及代码量
    file_lines_dict = {}
    # 判断目录或文件是否存在
    if not os.path.exists(count_path):
        print("输入的目录或文件不存在")

    # 判断是否是文件
    if os.path.isfile(count_path):
        # 获取文件类型，如果bb.py中的.py
        file_type = os.path.splitext(count_path)[1]
        # 如果文件类型在指定的文件类型中，调用统计单个文件的函数，统计单个文件代码
        if file_type in file_types:
            total_line_number = count_sigle_file_code(count_path)
        # 单个文件及代码量写入字典
        file_lines_dict[count_path] = total_line_number
        # 返回文件代码量 及文件字典
        return "文件 %s代码行数: %d" % (count_path, total_line_number)
    # 判断是否是目录
    elif os.path.isdir(count_path):
        # 遍历目录下的所有文件
        for root, dirs, files in os.walk(count_path):
            for file in files:
                # 获取文件绝对路径
                file_path = os.path.join(root, file)
                # 获取文件类型，如果bb.py中的.py
                file_type = os.path.splitext(file_path)[1]

                # 如果文件类型在指定的文件类型中，调用统计单个文件的函数，统计单个文件代码
                if file_type in file_types:
                    file_line_number = count_sigle_file_code(file_path)
                    # 累计同代码量
                    total_line_number += file_line_number
                # 单个文件及代码量写入字典
                file_lines_dict[file_path] = file_line_number

        # 返回总代码量及文件字典
        return "总文代码行数: %d\n每个文件的代码行数: %s" % (total_line_number, file_lines_dict)


# 总计单个文件代码量
def count_sigle_file_code(file_path):
    # 记录单个文件代码量
    line_number = 0
    # 用于标记是否要记录多行注释代码行，True代码
    flag = True

    # 获取编码格式
    try:
        fp = open(file_path, encoding="utf-8")
        encoding_type = "utf-8"
    except:
        encoding_type = "gbk"
    finally:
        fp.close()

    # 打开文件统计代码
    with open(file_path, encoding=encoding_type) as file_obj:
        for line in file_obj:
            # 去除每行文件两端的空白
            line = line.strip()

            # 如果以三引号结尾且falg==False，需要把flag置为True，证明跳出多行注释了
            # 同时跳过本行，不统计
            if line.endswith("'''") and flag == False:
                flag = True
                continue
            # flag==False证明在多行注释内部，跳过不统计
            elif flag == False:
                continue
            # 检测到多行注释结尾，且flag==False(之前在多行注释内部)
            # flag置为True，跳出多行注释
            elif line.endswith('"""') and flag == False:
                flag = True
                continue

                # 记录文件编码声明行
            elif line.startswith("#encoding") or line.startswith("#coding") \
                    or line.startswith("#-*-"):
                line_number += 1

            # 空行跳过不统计
            elif line == "":
                continue
            # 单行注释跳过不统计
            elif line.startswith("#"):
                continue

            # 在一行的三引号注释跳过，不统计；以三引号开头且此行不等于三引号
            elif line.startswith("'''") and line.endswith("'''") and line != "'''":
                continue

            # 在一行的三引号注释跳过，不统计；以三引号开头且此行不等于三引号
            elif line.startswith('"""') and line.endswith('"""') and line != '"""':
                continue

            # 检测到多行注释的开头
            # 如果flag等于True,需要把flag置为False，以便接下来不统计多行注释内的代码
            elif line.startswith("'''") and flag == True:
                flag = False
                continue
            # 同上
            elif line.startswith('"""') and flag == True:
                flag = False
                continue
            # 排序不统计的情况,累计代码行
            else:
                line_number += 1
    # 返回代码行
    return line_number


if __name__ == "__main__":
    # 控制台执行名利格式:E:\python>py -3 a.py d:\test\bb.py  .py
    # 执行文件  统计目录或文件  文件类型
    import sys

    # 如果长度小于2，证明没有输入目录
    if len(sys.argv) < 2:
        print("请输入要统计的文件目录")
        sys.exit()
    # 获取需要统计的文件目录或文件
    count_path = sys.argv[1]
    # 文件类型列表
    file_types = []

    # 如果命令行参数list长度大于2，证明有目录和文件类型
    if len(sys.argv) > 2:
        # 遍历命令行的文件类型，加入列表
        for file_type in sys.argv[2:]:
            file_types.append(file_type)
    # print(count_path,file_types)
    # 调用统计代码行函数
    print(count_all_file_code(count_path, file_types))