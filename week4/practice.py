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

def baseConvert(n, base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        pass