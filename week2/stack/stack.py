# -*- coding: utf-8 -*
import time


class Stack1:  # Python实现ADT stack，栈尾实现

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


# 实现方法2，栈顶实现
class Stack2:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    count_time1 = 0
    count_time2 = 0
    for i in range(10000):
        start_time = time.perf_counter()
        s = Stack1()
        s. push('dog')
        s.push(True)
        s.push(8.4)
        s.pop()
        finish_time = time.perf_counter()
        count_time1 += finish_time - start_time

        start_time = time.perf_counter()
        s = Stack2()
        s. push('dog')
        s.push(True)
        s.push(8.4)
        s.pop()
        finish_time = time.perf_counter()
        count_time2 += finish_time - start_time

    print("方法一运行时间 %s" % count_time1)
    print("方法二运行时间 %s" % count_time2)

"""
程序运行时间
    方法一运行时间 0.01718990000000087
    方法二运行时间 0.020802599999999394
"""