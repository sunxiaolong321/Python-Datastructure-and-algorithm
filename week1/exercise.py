# -*- coding: utf-8 -*
import time

"""
问题描述
    所谓“变位词”是指两个词之间存在组成字母的重新排列关系
    如: heart 和earth, python和typhon
    为了简单起见，假设参与判断的两个词仅由小写字母构成，而且长度相等

解题目标
    写一个bool函数，以两个词作为参数，返回这两个词是否变位词

可以很好展示同一问题的不同数量级算法
"""


def anagramSolution1(s1, s2):   # 遍历方法，逐字检查
    alist = list(s2)
    pos1 = 1
    StillOk = True
    while pos1 < len(s1) and StillOk:   # 循环s1的字符
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:     # 在s2逐个对比
                found = True
            else:
                pos2 = pos2 + 1
        if found:
            alist[pos2] = None      # 找到，打钩
        else:
            StillOk = False  # 未找到，失败
        pos1 += 1
    return StillOk


def anagramSolution2(s1, s2):   # 排序比较
    alist1 = sorted(s1)
    alist2 = sorted(s2)

    pos = 0
    matches = True
    while pos < len(s1) and matches:
        if alist1[pos] == alist2[pos]:
            pos += 1
        else:
            matches = False
    return matches


def anagramSolution3(s1, s2):   # 计数比较
    c1 = [0]*26     # 映射字母到列表中
    c2 = [0]*26

    for i in range(len(s1)):

        pos = ord(s1[i]) - ord('a')     # 字母个数统计  
        c1[pos] += 1
    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] += 1
    j = 0
    StillOk = True
    while(j < 26) and StillOk:
        if c1[j] == c2[j]:
            j += 1
        else:
            StillOk = False
    return StillOk


if __name__ == "__main__":
    counter_time1 = 0
    counter_time2 = 0
    counter_time3 = 0
    for i in range(10000):

        start_time = time.perf_counter()
        anagramSolution1("python", "typhon")
        end_time = time.perf_counter()
        counter_time1 += end_time-start_time

        start_time = time.perf_counter()
        anagramSolution2("python", "typhon")
        end_time = time.perf_counter()
        counter_time2 += end_time-start_time

        start_time = time.perf_counter()
        anagramSolution3("python", "typhon")
        end_time = time.perf_counter()
        counter_time3 += end_time-start_time

    print("程序运行10000次时间%sS" % counter_time1)
    print("程序运行10000次时间%sS" % counter_time2)
    print("程序运行10000次时间%sS" % counter_time3)
'''
程序运行时间
    程序运行10000次时间0.06652659999999812S
    程序运行10000次时间0.028769400000001236S
    程序运行10000次时间0.0948885999999989S
'''
