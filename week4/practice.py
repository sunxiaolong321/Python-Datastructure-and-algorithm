# -*- coding:utf-8 -*

"""
题目内容：
    给定一个M进制的数，请将其转换为N进制并输出
输入格式:
    两行，第一行为空格分隔的两个数字，分别为10进制表示的M与N；其中M, N均满足2 ≤ M、N ≤ 36
    第二行为待转换的数字，其中每位超过9的部分从10至36分别用大写字母A-Z表示；输入数据保证其中最大位数对应数字不超过M
输出格式：
    一行字符串，表示转换后的N进制数
输入样例：
    8 16
‭   473‬
输出样例：
    ‭13B‬
"""

# 题目没看懂，尴了个尬
# def baseConvert(n, base):
#     convertString = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     if n < base:
#         return convertString[n]
#     else:
#         return baseConvert(n//base, base) + convertString[n % base]
"""
题目内容：
    如课上所说，汉诺塔问题源于印度一个古老传说。对于原始的汉诺塔游戏，
    可供玩家操作的空间一共只有三根柱子，导致按原传说的要求，需要超过
    1.8*10 ^ 19步才能解开。
    透过新增柱子可以大幅度地减少需要的步数。此处要求在给出指定的盘数，
    柱子数量为4（即限制为4根柱子）且不改变原有传说的其他规则的限制下
    ，找出完成迁移的最小步骤数。
输入格式:
    一个非负整数M，M代表盘数，M <= 1000。
输出格式：
    一个非负整数，表示完成迁移的最小步骤数。
输入样例：
    3
输出样例：
    5
"""
# count = 0


def moveTower(m, fromPole, withPole1, withPole2, toPole):
    if m == 1:
        global count
        count += 1
    else:
        moveTower(m//2, fromPole, withPole2, toPole, withPole1)
        moveTower3(m-m//2, fromPole, withPole1, withPole2, toPole)
        moveTower(m//2, withPole1, withPole2, toPole, fromPole)


def moveTower3(m, fromPole, withPole1, withPole2, toPole):
    if m == 1:
        global count
        count += 1
    else:
        moveTower3(m-1, fromPole, withPole1, toPole, withPole2)
        count += 1
        moveTower3(m-1, withPole2, fromPole, withPole1, toPole)

# moveTower(eval(input()), "#1", "#2", "#3", "#4")
# print(count)


"""
题目内容：
    谢尔宾斯基地毯是形如上图的正方形分形图案，每个地毯可分为等大小的9份，其中中央挖空，其余均由更小的地毯组成。
    现给定地毯大小（行数）与组成地毯的字符元素，请打印相应的地毯图形。
    注：空腔以半角空格表示；当给定字符元素长度不为1时空格数须与字符长度对应
输入格式:
    输入为两行，分别为地毯大小正整数N与组成元素字符串c
    输入数据保证N为3的正整数幂
输出格式：
    由N行长度为N*len(c)的字符串构成的谢尔宾斯基地毯
    例如
    [][][][][][][][][]
    []  [][]  [][]  []
    [][][][][][][][][]
    [][][]      [][][]
    []  []      []  []
    [][][]      [][][]
    [][][][][][][][][]
    []  [][]  [][]  []
    [][][][][][][][][]
输入样例：
    9
    []
"""


def mark(x, y, C):
    if y % 3 == 1 and x % 3 == 1:
        print(" "*len(C), end="")
    else:
        print(C, end="")


def carpet(N, C):
    for i in range(N):
        for j in range(N):
            mark(i, j, C)
        print()


N = 27
C = "[]"
carpet(N, C)
