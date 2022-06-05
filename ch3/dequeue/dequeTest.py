#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2021/12/13 23:32:51
@Author  : Zhaopeng SHI
@Email   : zhaopshi@gmail.com
@File    : dequeTest.py
"""

# here put the import lib
import numpy as np

class Deque():
    def __init__(self):
        self.items = []

    def addFront(self, item):
        self.items.append(0, item)

    def addRear(self, item):
        self.items.append(item)

    def removeFront(self):
        return self.items.pop()
    
    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

def palchecker(aString):
    checkingDeque = Deque()

    for ch in aString:
        checkingDeque.addRear(ch)

    isEqueal = True

    while isEqueal and checkingDeque.size() > 1:
        first = checkingDeque.removeFront()
        last = checkingDeque.removeRear()
        if first != last:
            isEqueal = False

    return isEqueal

def main():
    print(palchecker('abcdedcba'))
    print(palchecker('11111dssds'))

    return 0

if __name__ == '__main__':
    main()