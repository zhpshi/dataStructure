#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time    : 9/1/2022 11:37 PM
@Author  : Zhaopeng SHI
@Email   : zhaopshi@gmail.com
@File    : orderedlist.py
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

class OrderedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        temp = Node(item)
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
            if previous == None:
                temp.setNext(current)
                self.head = temp
            else:
                temp.setNext(current)
                previous.setNext(temp)





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
        stop = False
        while current != None and found == False and not stop:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
            if current.getData() > item:
                return False

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
    return 0


if __name__ == '__main__':
    main()
