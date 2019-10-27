# -*- coding:utf-8 -*


class Node:     # 节点实现
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getCurrent(self):
        return self.data

    def getNext(self):
        return self.next

    def addCurrent(self, item):
        self.data = item

    def addNext(self, item):
        self.next = item


class unorderedList:     # 无序列表实现
    def __init__(self):
        self.head = None

    def printer(self):
        current = self.head
        while current != None:
            print(current.getCurrent(), end="\t")
            current = current.getNext()

    def append(self, item):
        temp = Node(item)
        temp.addNext(self.head)
        self.head = temp

    def isEmpty(self):  # 判断是否为空
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def search(self, item):  # 搜索函数
        current = self.head
        found = False
        while current != None and not found:
            if current.getCurrent() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def pop(self):  # pop()函数
        if self.head != None:
            self.head = self.head.getNext()
        else:
            return None

    def remove(self, item):
        current = self.head

        previous = None
        found = False
        while current != None and not found:
            if current.getCurrent() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        
        if previous == None and current == None:
            return None
        elif previous == None:  # 直接找到
            self.head = current.getNext()
        elif current == None:  # 未找到
            return None
        else:
            previous.addNext(current.getNext())

    def pop(self, pos):
        current = self.head
        previous = None
        count = 0
        found = False
        while current != None and not found:
            if count == pos:
                found = True
            else:
                previous = current
                current = current.getNext()
                count += 1

        if previous == None and current == None:
            return None
        elif previous== None:
            self.head = current.getNext()
        elif current == None:
            return None
        else:
            previous.addNext(current.getNext())

    def index(self):
        count = 0
        current = self.head
        while current != None:
            current.getNext()
            count += 1
        
        return count

    def insert(self, pos, item):
        current = self.head
        previous = None
        found = False
        count = 0
        while current!= None and not found:
            if count == pos:
                found = True
            else:
                previous =current
                current = current.getNext()
                count += 1

        temp = Node(item)
        if previous == None and current == None:
            self.head = temp
        elif previous == None:
            self.head = temp
            temp.addNext(current)
        elif current == None:
            return None
        else:
            previous.addNext(temp)
            temp.addNext(current)


class orderedList:
    def __init__(self):
        self.head = None
    
    def append(self, item):
        current = self.head
        previous = None
        found = True
        while not found and current != None:
            if item < current.getCurrent():
                found = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous == None:
            temp.getNext(current)
            self.head = temp
        else:
            temp.getNext(current)
            previous.getNext(temp)
        
if __name__ == "__main__":
    x = unorderedList()
    x.append(1)
    x.append(2)
    x.append(4)
    x.insert(5,6)
    x.printer()
