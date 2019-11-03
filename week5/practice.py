# -*- coding:utf-8 -*
"""
给定一个长度为N的区域，及4种不同长度的瓷砖：
    灰瓷砖（长为1格）、红瓷砖（长为2格）、
    绿瓷砖（长为3格）与蓝瓷砖（长为4格），
    求所有不同的铺满整个区域的方法数。
    例如：当N = 5时，共有15种铺满区域的方法，示意图如下：
输入格式:
    一个自然数N
输出格式：
    一行数字，表示不同的方法总数
输入样例：
    5
输出样例：
    15
"""


def put(N, ceramicTileList, count):
    def putCeramicTile(N, ceramicTileList, count):
        if N == 0:
            count += 1
        else:
            for i in [c for c in ceramicTileList if c <= N]:
                count = putCeramicTile(N-i, ceramicTileList, count)  # 递归余下砖块
        return count
    if N == 0:
        return 0
    else:
        return putCeramicTile(N, ceramicTileList, count)


def dfs(N):
    if N == 0:
        return 0
    if N == 1:
        return 1
    if N == 2:
        return 1 + dfs(N-1)
    if N == 3:
        return 1 + dfs(N-1) + dfs(N-2)
    if N == 4:
        return 1 + dfs(N-1) + dfs(N-2) + dfs(N-3)
    else:
        return dfs(N-1) + dfs(N-2) + dfs(N-3) + dfs(N-4)


# for N in range(10):
#     print(put(N, [1, 2, 3, 4], 0))

"""
题目内容：
    老师想给孩子们分发糖果，有 N 个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。
    你需要按照以下要求，帮助老师给这些孩子分发糖果：
    每个孩子至少分配到 1 个糖果。
    相邻的孩子中，评分高的孩子必须获得更多的糖果。
    那么这样下来，老师至少需要准备多少颗糖果呢？
    输入格式:
    一个列表，以文本格式的有效Python表达式给出
输出格式：
    一行数字，表示满足分配条件所需的最少糖果数
输入样例：
    [1, 2, 2]
输出样例：
    4
    注：可行的分配方案为1、2、1 颗糖果；第三个孩子只得到1颗糖果也满足题目条件
"""
"""
    左右遍历观点
        先没人给一个苹果
        从左向右遍历一遍，再从右向左遍历一遍
        从右向左遍历中，左侧高于右侧，但左侧苹果比右侧少
        左边的数目为右边的数目+1
"""


def candy(ratings):
    distributions = [1]*len(ratings)
    for i in range(1, len(ratings)):
        if ratings[i] > ratings[i-1]:
            distributions[i] += 1
    for j in range(1, len(ratings)):
        if ratings[len(ratings)-j-1] > ratings[len(ratings)-j] and distributions[len(ratings)-j-1] <= distributions[len(ratings)-j]:
            distributions[len(ratings)-j-1] = distributions[len(ratings)-j]+1
    count = 0
    for distribution in distributions:
        count += distribution
    return count


# lst = eval(input())
# print(candy(lst))

"""
链接：https://www.nowcoder.com/questionTerminal/74a62e876ec341de8ab5c8662e866aef
来源：牛客网
    1）当前孩子的rating比前面的孩子的rating高时：
        只需要考虑当前孩子的candies数目比前面孩子的candies的数目多至少一个即可；
        当前面的rating等于后面孩子的rating时，则题目没有说明，则可以比他多或者少；
    2）当前孩子的rating比后面孩子的raitng低时：
        考虑当前孩子的后面的单调递减的孩子的数目，
        因为最后一个单调递减的孩子的手里至少还剩下一个糖果存在，
        则新建一个数组来存储单调递减孩子的数目，
        并将当前孩子的手里的糖果的数目设定为单调递减孩子的数目+1；
    3）判断左边动态规划和右边动态规划的糖果数目，取其中糖果数目最大的即可；
"""


def dynamicCandy(ratings):
    length = len(ratings)
    if length == 0:
        return 0
    distributions = [0]*length  # 存每个小孩应发的糖果树木
    distributions[0] = 1
    for i in range(1, length):  # 不断遍历ratings并更新distributions
        if ratings[i] > ratings[i-1]:   # 如果新加入的小孩大于前一个小孩，则糖果比前一个小孩多一个
            distributions[i] = distributions[i-1] + 1
        elif ratings[i] == ratings[i-1]:    # 如果等于前一个小孩，则新小孩需要分一个糖果，distributions不需要更新
            distributions[i] = 1

        else:   # 如果小于前一个小孩，则新加入的小孩分一个糖果，之前的小孩应该比他分到的糖果多
            distributions[i] = 1
            if distributions[i - 1] == 1:   # 如果前面的小孩只有一个糖果，则需要更新distributions
                j = i-1  # 前面的小孩都多分一个糖果，直到递增结束
                while j != 0 and distributions[j] < distributions[j-1]:
                    distributions[j] += 1
                    j -= 1
                if distributions[j] <= distributions[j+1] and\
                        distributions[j] != distributions[j+1]:    # ratings 相等情况
                    distributions[j] += 1

    sum = 0
    for distribution in distributions:
        sum += distribution
    return sum


# lst = eval(input())
# print(dynamicCandy(lst))

"""
题目内容：
    给定一个表达式字符串，求出按不同的求值顺序可能得到的所有结果
输入格式:
    一行字符串，仅包含0-9与运算符+、-与*
    注：字符串保证三种运算符左右均为数字字符
输出格式：
    所有不重复的可能的结果，从小到大排序并以半角逗号","分隔
输入样例：
    2*3-4*5
输出样例：
-34,-14,-10,10
注：
    (2*(3-(4*5))) = -34 
    ((2*3)-(4*5)) = -14 
    ((2*(3-4))*5) = -10 
    (2*((3-4)*5)) = -10 
    (((2*3)-4)*5) = 10
"""


def findWays(expr):
    # 用于将字符串转为数字与运算符，供参考
    nums, ops = [], []
    num = 0
    for c in expr:
        if '0' <= c <= '9':
            num = num * 10 + ord(c) - 48
        else:
            ops.append(c)
            nums.append(num)
            num = 0
    else:
        nums.append(num)

    def diffWaysToComputer(nums, ops):   # 使用递归运算
        if not ops:
            return [nums[0]]
        if len(ops) == 1:
            if ops[0] == '+':
                return nums[0]+nums[1]
            elif ops[0] == '-':
                return nums[0]-nums[1]
            else:
                return nums[0]*nums[1]
            res = []
            for i in range(len(ops)):
                result = diffWaysToComputer(nums[:i+1], ops[:i])
    return diffWaysToComputer(nums, ops)


expr = "2*3-4*5"
print(findWays(expr))
