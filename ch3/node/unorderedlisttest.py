#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time    : 3/1/2022 11:50 PM
@Author  : Zhaopeng SHI
@Email   : zhaopshi@gmail.com
@File    : unorderedlisttest.py
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


class UnorderedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        count = 0
        current_node = self.head
        while current_node != None:
            count += 1
            current_node = current_node.getNext()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and found == False:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
                self.head = current.getNext()
        else:
                previous.setNext(current.getNext())


def main():

    mylist = UnorderedList()
    print(mylist.head)
    return 0


if __name__ == '__main__':
    main()
