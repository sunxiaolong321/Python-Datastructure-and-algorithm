# -*- coding : utf-8 -*


class Queue1:  # 队列实现方法1，尾部添加元素
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


class Queue2:   # 队列实现方法2，头部添加元素
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


def hotPotato(namelist, num):    # 热土豆问题
    simqueque = Queue2()
    for name in namelist:
        simqueque.enqueue(name)

    while simqueque.size() > 1:
        for i in range(num):
            simqueque.enqueue(simqueque.dequeue())  # 将不符合条件的土豆重新加入到队列
        simqueque.dequeue()

    return simqueque.dequeue()


if __name__ == "__main__":
    print(hotPotato(["Bill", "IDavid", "Susan", "Jane", "Kent", "Brad", "Dnaial"], 7))
