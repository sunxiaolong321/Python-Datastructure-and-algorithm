# -*- coding:utf-8 -*
"""
模拟算法: 打印任务
一个具体的实例配置如下:
    一个实验室，在任意的一个小时内，大约有10名学生在场,
    这一小时中，每人会发起2次左右的打印，每次1~20页。
    打印机的性能是:以草稿模式打印的话，每分钟10页，
    以正常模式打印的话，打印质量好，但速度下降
    为每分钟5页。
"""
import random
from queue import Queue


class Printer():
    def __init__(self, ppm):
        self.pagerate = ppm     # 打印速度
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining -= 1
        if self.timeRemaining <= 0:
            self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self, newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages()*60/self.pagerate


class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):
        return currenttime - self.timestamp


def newPrintTask():
    num = random.randrange(1, 181)  # 1/180的概率完成任務
    if num == 180:
        return True
    else:
        return False


def simulation(numSeconds, pagesPerMinute):
    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):
        if newPrintTask():
            task = Task(currentSecond)
            printQueue.put(task)

        if (not labprinter.busy()) and (not printQueue.empty()):
            nexttask = printQueue.get()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)
    
    labprinter.tick()

    avarageWait = sum(waitingtimes)/len(waitingtimes)
    print("Average Wait %6.2fsecs %3d tasks remaining." % (avarageWait, printQueue.qsize()))

if __name__ == "__main__":
    for i in range(10):
        simulation(3600, 10)
