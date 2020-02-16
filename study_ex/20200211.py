#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 256、给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
# 给定 nums = [2, 7, 11, 15], target = 9
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
# def find_aims(p, aims):
#     res = []
#     for i in range(len(p)):
#         for j in range(i+1, len(p)):
#             if p[i] + p[j] == aims:
#                 res.append(i)
#                 res.append(j)
#     return res
#
#
# print(find_aims([2, 7, 11, 15], 9))


# 257、给定两个大小为 m 和 n 的有序数组 nums1 和 nums2 。
# 请找出这两个有序数组的中位数。要求算法的时间复杂度为 O(log (m+n)) 。
# 你可以假设 nums1 和 nums2 不同时为空。
# def findMedianSortedArrays(nums1, nums2):
#     nums = sorted(nums1 + nums2)
#     if len(nums) % 2 == 1:
#         return nums[len(nums) // 2]
#     else:
#         return (nums[len(nums) // 2 - 1] + nums[len(nums) // 2]) / 2
#
#
# print(findMedianSortedArrays([4,6], [5,6,8,9,56,534]))


# 258、给定一个字符串，找出不含有重复字符的最长子串的长度。
# 示例 1:
# 输入: "abcabcbb"输出: 3 解释: 无重复字符的最长子串是 "abc"，其长度为 3。
# 示例 2:
# 输入: "bbbbb"输出: 1解释: 无重复字符的最长子串是 "b"，其长度为 1。
# 示例 3:
# 输入: "pwwkew"输出: 3解释: 无重复字符的最长子串是 "wke"，其长度为 3。
#      请注意，答案必须是一个子串，"pwke" 是一个子序列 而不是子串
# def find_no_duplication(s):
#     sub_list = []
#     res = []
#     for i in range(len(s)):
#         for j in range(len(s)-1):
#             sub_list.append(s[i:i + j + 1])
#     for k in sub_list:
#         if len(list(k)) == len(set(list(k))):
#             res.append(k)
#     print(sorted(res, key=len))
#     return sorted(res, key=len)[-1]
#
#
# print(find_no_duplication("abcabcbb"))
# print(find_no_duplication("bbbbb"))
# print(find_no_duplication("pwwkew"))


# 259、给定一个 32 位有符号整数，将整数中的数字进行反转
# def reverse(x):
#     if x >= 0:
#         x = str(x)
#         x = int(x[::-1])
#         if x > (-2) ** 31 and x < 2 ** 31 - 1:
#             return x
#         else:
#             return 0
#     elif x < 0:
#         x = str(x)
#         x = x[1:]
#         x = 0 - int(x[::-1])
#         if x > (-2) ** 31 and x < 2 ** 31 - 1:
#             return x
#         else:
#             return 0


# 260、实现 atoi，将字符串转为整数。
# 该函数首先根据需要丢弃任意多的空格字符，直到找到第一个非空格字符为止。
# 如果第一个非空字符是正号或负号，选取该符号，并将其与后面尽可能多的连续的数字组合起来，这部分字符即为整数的值。
# 如果第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。
# 字符串可以在形成整数的字符后面包括多余的字符，这些字符可以被忽略，它们对于函数没有影响。
# 当字符串中的第一个非空字符序列不是个有效的整数；或字符串为空；或字符串仅包含空白字符时，则不进行转换。
# 若函数不能执行有效的转换，返回 0。
#     def myAtoi(self, str):
#         """
#         :type str: str
#         :rtype: int
#         """
#         # 出去原字符串两端的空白
#         str = str.strip()
#         # 字符串为空、字符串为单个+-,返回0
#         if str == "" or str in "+-":  # 子符串为空或为一个+-
#             return 0
#         # 子符串首字符不是-+并且首字符也不是数字的话，返回0
#         elif str[0] not in "-+" and not str[0].isdigit():
#             return 0
#         # 字符串首字符是-+,但是第二个字符不是数字的话，返回0
#         elif str[0] in "-+" and not str[1].isdigit():
#             return 0
#         # 如果首字符是-+，且第二个字符不是-+
#         if str[0] in "-+" and str[1] not in "-+":
#             tmpStr = ""
#             # 判断从第二个字符开始是否是数字
#             for v in str[1:]:
#                 if v.isdigit():
#                     tmpStr += v
#                 else:
#                     break
#             # 取到数字字符串后需要判断是正数还是负数
#             # 如果是正数，且不大于最大值的话返回字符串的整数表示，否则返回最大数
#             if str[0] == "+":
#                 if int(tmpStr) > (2 ** 31 - 1):
#                     return 2 ** 31 - 1
#
#                 else:
#                     return int(tmpStr)
#                     # 如果是负数，且不小于最小值的话返回字符串的整数表示，否则返回小数
#             else:
#                 if (0 - int(tmpStr)) < (-2) ** 31:
#                     return (-2) ** 31
#                 else:
#                     return 0 - int(tmpStr)
#         # 如果首字符是数字，拼接后续数字并返回
#         elif str[0].isdigit():
#             tmpStr = ""
#             for v in str:
#                 if v.isdigit():
#                     tmpStr += v
#                 else:
#                     break
#             # 如果大于最大值，返回最大值
#             if int(tmpStr) > (2 ** 31 - 1):
#                 return 2 ** 31 - 1
#
#             else:
#                 return int(tmpStr)
