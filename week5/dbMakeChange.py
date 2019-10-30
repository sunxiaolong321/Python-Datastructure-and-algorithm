# -*- coding:utf-8 -*
"""
-个经典案例是兑换最少个数的硬币问题
    假设你为一家自动售货机厂家编程序，自动售货
    机要每次找给顾客最少数量硬币；
    假设某次顾客投进$1纸币，买了37的东西，要
    找63，那么最少数量就是: 2个quarter(25)
    1个dime(c10)和3个penny(e1) ，一共6个
"""


def dpMakeChange(coinValueList, change, minCoins):  # 动态规划法解决问题
    for cents in range(1, change + 1):
        coinCount = cents
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents - j] + 1
        minCoins[cents] = coinCount
    return minCoins[change]


print(dpMakeChange([1, 5, 10, 21, 25], 63, [0]*64))
