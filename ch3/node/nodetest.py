#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time    : 3/1/2022 11:13 PM
@Author  : Zhaopeng SHI
@Email   : zhaopshi@gmail.com
@File    : nodetest.py
"""


# import package here

class Node:
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


def main():
    test = Node(1)
    print(test.getData())
    return 0


if __name__ == '__main__':
    main()
