# -*- coding: utf-8 -*


class Node:  # 节点实现
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class UnorderedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getData

        return found

    def remove(self, item):
        current = self.head
        pervious = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                pervious = current
                current = current.getNext()

        if pervious == None:
            self.head = current.getNext()
        else:
            pervious.setNext(current.getNext())


# if __name__ == "__main__":
#     x = UnorderedList()
#     x.add(123)
#     print(x.size())

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


class queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


def func(mylist):
    queue0 = queue()
    queue1 = queue()
    queue2 = queue()
    queue3 = queue()
    queue4 = queue()
    queue5 = queue()
    queue6 = queue()
    queue7 = queue()
    queue8 = queue()
    queue9 = queue()
    queueMain = queue()

    for value in mylist:
        queueMain.enqueue(value)

    for i in range(1, 4):
        while queueMain.size() > 0:
            value = queueMain.dequeue()
            if value % (10*i) == 1:
                queue1.enqueue(value)
            elif value % (10*i) == 2:
                queue2.enqueue(value)
            elif value % (10*i) == 3:
                queue3.enqueue(value)
            elif value % (10*i) == 4:
                queue4.enqueue(value)
            elif value % (10*i) == 5:
                queue5.enqueue(value)
            elif value % (10*i) == 6:
                queue6.enqueue(value)
            elif value % (10*i) == 7:
                queue7.enqueue(value)
            elif value % (10*i) == 8:
                queue8.enqueue(value)
            elif value % (10*i) == 9:
                queue9.enqueue(value)
            elif value % (10*i) == 0:
                queue0.enqueue(value)

        while queue0.size() > 0:
            queueMain.enqueue(queue0.dequeue())
        while queue1.size() > 0:
            queueMain.enqueue(queue1.dequeue())
        while queue2.size() > 0:
            queueMain.enqueue(queue2.dequeue())
        while queue3.size() > 0:
            queueMain.enqueue(queue3.dequeue())
        while queue4.size() > 0:
            queueMain.enqueue(queue4.dequeue())
        while queue5.size() > 0:
            queueMain.enqueue(queue5.dequeue())
        while queue6.size() > 0:
            queueMain.enqueue(queue6.dequeue())
        while queue7.size() > 0:
            queueMain.enqueue(queue7.dequeue())
        while queue8.size() > 0:
            queueMain.enqueue(queue8.dequeue())
        while queue9.size() > 0:
            queueMain.enqueue(queue9.dequeue())
    
    return queueMain.items


mylist = eval(input())
print(func(mylist))
