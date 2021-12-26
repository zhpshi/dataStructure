#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time    : 2021/12/12 23:35:44
@Author  : Zhaopeng SHI
@Email   : zhaopshi@gmail.com
@File    : print_sim.py
'''

# here put the import lib
import random

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self, newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60 / self.pagerate #newtask is a variable whose class is Task(defined in following)

class Task:
    def __init__(self, time):
        self.timetamp = time
        self.pages = random.randrange(1,21)
    
    def getStamp(self):
        return self.timetamp
    
    def getPages(self):
        return self.pages
    
    def waitTime(self, currenttime):
        return currenttime - self.timetamp
    
def newPrintTask():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False

def simulation(numSeconds, pagesPerMinute):
    
    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtime = []

    for currentSecond in range(numSeconds):

        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)
        
        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtime.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)
        
        labprinter.tick()

    everageWait = sum(waitingtime) / len(waitingtime)
    print('Average Wait %6.2f secs %3d tasks remaining.'% (everageWait, printQueue.size()))

def main():
    for i in range(10):
        simulation(3600, 5)
    return 0

if __name__ == '__main__':
    main()