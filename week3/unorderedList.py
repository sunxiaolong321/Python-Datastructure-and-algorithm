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

    def pop(self):
        current = self.head
        self.head = current.getNext()

    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count != 1
        return count

    def index(self, item):
        current = self.head
        previous = None
        index = 0
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
                index += 1

        return index

    def insert(self, pos, item):
        current = self.head
        previous = None
        index = 0
        while pos:
            previous = current
            current.getNext()
            pos -= 1

        node = Node(item)
        if previous == None:
            self.head = node
        else:
            previous.getNext(node)
        node.getNext(current)

    def pop(self, pos):
        current = self.head
        previous = None
        while pos:
            previous = current
            current.getNext()
            pos -= 1

        if previous == None:
            self.head = current.getNext()
        else:
            previous.getNext(current.getNext())
