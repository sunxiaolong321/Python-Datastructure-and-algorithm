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
#     minStr = S
#     for i in range(len(S)-1):
#         S = "".join([S[1:],S[0]])
#         if minStr > S:
#             minStr = S
#     return minStr


# S = eval(input())
# print(func(S))

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

#     resultList = list()
#     for i in range(len(mylist)):
#         count = 1
#         for j in range(i):
#             if mylist[j] <= mylist[i] and mylist[j] >= mylist[i] - 10000:
#                 count += 1
#         resultList.append(count)
#     return resultList


# mylist = eval(input())
# print(func(mylist))


"""
题目内容：
    实现一个基数排序算法，用于10进制的正整数从小到大的排序。
    思路是保持10个队列(队列0、队列1......队列9、队列main)，
    开始，所有的数都在main队列，没有排序。
    第一趟将所有的数根据其10进制个位(0~9)，放入相应的队列0~9，
    全放好后，按照FIFO的顺序，将每个队列的数合并排到main队列。
    第二趟再从main队列队首取数，根据其十位的数值，放入相应队列0~9，
    全放好后，仍然按照FIFO的顺序，将每个队列的数合并排到main队列。
    第三趟放百位，再合并；第四趟放千位，再合并。
    直到最多的位数放完，合并完，这样main队列里就是排好序的数列了。
输入格式:
    一个列表mylist，其中mylist包含一些需要排序的正整数，
    正整数互不相同且均不超过100000，且个数在1至1000之间。
输出格式：
    一个与mylist等长的列表。
输入样例：
    [8, 91, 34, 22, 65, 30, 4, 55, 18]
输出样例：
    [4, 8, 18, 22, 30, 34, 55, 65, 91]
"""


class func(mylist):
    dictItem = {}
    


mylist = eval(input())
print(func(mylist))
