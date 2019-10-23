"""
题目内容：
    一开始给出了一个由小写字母组成的字符串 S。
    我们规定每次移动中，选择最左侧的字母，将其从原位置移除，
    并加到字符串的末尾。这样的移动可以执行任意多次
    返回我们移动之后可以拥有的最小字符串
    （注：在Python3中，字符串的大小可用不等号比较）。
输入格式:
    S。S为仅含有小写字母的字符串，长度不超过100000。
    输出格式：
    一个与S等长的字符串。
输入样例：
    "cba"
输出样例：
    acb
"""


# def func(S):
#     charList = list(S)
#     for i in range(len(charList)-1):
#         charList.append(charList.pop(0))
#     return "".join(charList)

# if __name__ == "__main__":
#     S = eval(input())
#     print(func(S))

"""
题目内容：
    计算每个事件发生之时，往前算10000毫秒内有多少个事件发生，包含当事件；
    也即对于列表中的每个元素k，算出整个列表中有多少个元素介于k-10000和k（两端均含）之间。
输入格式:
    一个已排序列表mylist，所有元素为非负整数，记录各个请求的发生时间，单位为毫秒。
输出格式：
    一个与mylist等长的列表。
输入样例：
    [0,10,100,1000,10000,20000,100000]
输出样例：
    [1,2,3,4,5,2,1]
"""


# def func(mylist):
#     # your code here
#     resultList = []
#     for element in mylist:
#         count = 0
#         for value in mylist:
#             if value <= element and value >= element - 10000:
#                 count += 1
#         resultList.append(count)
#     return resultList


# mylist = eval(input())
# print(func(mylist))
