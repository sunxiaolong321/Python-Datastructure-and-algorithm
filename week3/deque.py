# -*- coding:utf-8 -*

# 双端队列实现
class Deque:
    def __init__(self):
        self.items = []

    def addFront(self, item):   # 队首入队
        self.items.insert(0, item)

    def addRear(self, item):    # 队尾入队
        self.items.append(item)
    
    def removeFrond(self):    # 移除队首数据
        return self.items.pop(0)
    
    def removeRear(self): # 移除队尾数据
        return self.items.pop()
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)


# 回文词判断
def palchecker(aString):
    chardeque = Deque()

    for ch in aString:
        chardeque.addFront(ch)
    
    stillEqual = True
    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFrond()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False
    
    return stillEqual

if __name__ == "__main__":
    print(palchecker("lsdkjfskf"))
    print(palchecker("radar"))
