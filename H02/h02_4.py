#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time    : 27/1/2022 8:16 PM
@Author  : Zhaopeng SHI
@Email   : zhaopshi@gmail.com
@File    : h02_4.py
"""
# ======== 4 链表实现栈和队列 ========
# 用链表实现ADT Stack与ADT Queue的所有接口

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

class LinkStack:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def push(self, item):
        temp = Node(item)

        if self.head == None:
            self.head = temp
        else:
            temp.setNext(self.head)
            self.head = temp

    def pop(self):
        temp = self.head
        self.head = temp.getNext()
        return temp.getData()

    def peek(self):
        return self.head.getData()

    def size(self):
        count = 0
        temp = self.head
        while temp != None:
            temp = temp.getNext()
            count += 1
        return count

    def __str__(self):
        if self.head != None:
            temp_list = []
            temp = self.head
            while temp != None:
                temp_list.append(temp.getData())
                temp = temp.getNext()

            return 'A LinkStack: %s' % (','.join(str(item) for item in temp_list))
        else:
            return 'An empty LinkStack'

class LinkQueue():
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def enqueue(self, item):
        temp = Node(item)

        if self.head == None:
            self.head = temp
        else:
            temp.setNext(self.head)
            self.head = temp

    def dequeue(self):
        previous = self.head
        current = previous.getNext()
        if current == None:
            self.head = None
            return previous.getData()
        else:
            while current.getNext() != None:
                previous = current
                current = current.getNext()
            previous.setNext(None)
            return current.getData()

    def size(self):
        count = 0
        temp = self.head
        while temp != None:
            temp = temp.getNext()
            count += 1
        return count

    def __str__(self):
        if self.head != None:
            temp_list = []
            temp = self.head
            while temp != None:
                temp_list.append(temp.getData())
                temp = temp.getNext()

            return 'A LinkQueue: %s' % (','.join(str(item) for item in temp_list))
        else:
            return 'An empty LinkQueue'

def teststack():
    l = LinkStack()
    print(l.isEmpty())
    l.push('1')
    l.push('2')
    l.push('3')
    print(l)
    print(l.size())
    print(l.peek())
    print(l.pop())
    print(l)
    print(l.isEmpty())

def testqueue():
    l = LinkQueue()
    print(l.isEmpty())
    l.enqueue('1')
    l.enqueue('2')
    l.enqueue('3')
    print(l)
    print(l.size())
    print(l.dequeue())
    print(l)
    print(l.dequeue())
    print(l)
    print(l.dequeue())
    print(l)
    print(l.isEmpty())
def main():
    testqueue()
    teststack()
    return 0


if __name__ == '__main__':

    main()
