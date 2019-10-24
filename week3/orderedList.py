# -*- coding:utf-8 -*

class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def nextData(self):
        return self.next
    
    def setData(self, data):
        self.data = data
    
    def setNext(self, next):
        self.next = next

class OrderedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:    # 发现插入位置
                stop = True
            else:
                previous = current
                current = current.getNext()
        
        temp = Node(item)
        if previous == None:    # 插入在表头
            temp.setNext(self.head)
            self.head = temp
        else:   # 插入在表中
            temp.setNext(current)
            previous.setNext(temp)

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()
        
        return found