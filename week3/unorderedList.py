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


if __name__ == "__main__":
    x = UnorderedList()
    x.add(123)
    print(x.size())
