# -*- coding:utf-8 -*
import time
"""
-个经典案例是兑换最少个数的硬币问题
    假设你为一家自动售货机厂家编程序，自动售货
    机要每次找给顾客最少数量硬币；
    假设某次顾客投进$1纸币，买了37的东西，要
    找63，那么最少数量就是: 2个quarter(25)
    1个dime(c10)和3个penny(e1) ，一共6个
"""

# change为兑换金额，coinValueList为兑换金额
def greedyChange(coinValueList, change):  # 贪心策略解决硬币问题
    minCoins = change
    if change in coinValueList:
        return 1
    else:
        for i in [c for c in coinValueList if c < change]:
            numCoins = 1 + greedyChange(coinValueList, change-i)
        if numCoins < minCoins:
            minCoins = numCoins
    return minCoins

# print(time.process_time())
# print(greedyChange([1, 5, 10, 25], 63))
# print(time.process_time())


def NewGreedyChange(coinValueList, change, knownResults):  # 贪心策略解决硬币问题，消除重复计算
    minCoins = change
    if change in coinValueList:  # 最小规模，直接返回
        knownResults[change] = 1
        return 1
    elif knownResults[change] > 0:
        return knownResults[change] # 查表成功，直接用最优解，而不需要再次递归
    else:
        for i in [c for c in coinValueList if c <= change]:
            # 调用自身，减少规模，每次减去一种硬币面值挑选最小数量
            numCoins = 1 + NewGreedyChange(coinValueList, change-i, knownResults)
            if numCoins < minCoins:
                minCoins = numCoins
                knownResults[change] = minCoins
    return minCoins

# print(NewGreedyChange([1,5,10,25],63,[0]*64))
print(list(range(5)))