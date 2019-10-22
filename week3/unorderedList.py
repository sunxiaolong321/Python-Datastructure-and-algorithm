# -*- coding: utf-8 -*


class List:  # 创建无序列表
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        self.items.remove(item)

    def search(self, item):
        for char in self.items:
            if char == item:
                return True
        return False

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.itmes)

    def append(self, item):
        self.items.append(item)

    def index(self, item):
        for index in range(len(self.items)):
            if self.items[index] == item:
                return index
        return False

    def insert(self, pos, item):
        self.items.insert(pos, item)

    def pop(self):
        self.items.pop()

    def pop(self, pos):
        self.items.pop(pos)


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
