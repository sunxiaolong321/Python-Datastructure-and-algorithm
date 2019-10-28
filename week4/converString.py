# -*- coding:utf-8 -*


def toStr(n, base):  # 递归实现进制转换
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toStr(n//base, base)+convertString[n % base]

for i in range(1,50):
    print(toStr(i, 12))
