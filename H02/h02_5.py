#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time    : 27/1/2022 9:41 PM
@Author  : Zhaopeng SHI
@Email   : zhaopshi@gmail.com
@File    : h02_5.py
"""
# ======== 5 双链无序表 ========
# 实现双向链表版本的UnorderedList，接口同ADT UnorderedList
# 包含如下方法：isEmpty, add, search, size, remove, append，index，pop，insert, __len__, __getitem__
# 用于列表字符串表示的__str__方法 (注：__str__里不要使用str(), 用repr()代替
# 用于切片的__getitem__方法
# 在节点Node中增加prev变量，引用前一个节点
# 在UnorderedList中增加tail变量与getTail方法，引用列表中最后一个节点
# 选做：DoublyLinkedList(iterable) -> new DoublyLinkedList initialized from iterable's items
# 选做：__eq__, __iter__

# import package here
class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
        self.prev = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next
    
    def getPrev(self):
        return self.prev
    
    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext
    
    def setPrev(self, newprev):
        self.prev = newprev

class DoublyLinkedList:
    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        self.marker = self.head
        if iterable != None:
            try:
                if isinstance(iterable, list):
                    if len(iterable) == 0:
                        self.head = None
                        self.tail = None
                    elif len(iterable) == 1:
                        self.head = Node(iterable[0])
                        self.tail = self.head
                    else:
                        self.head = Node(iterable[0])
                        self.tail = Node(iterable[1])
                        self.head.setNext(self.tail)
                        self.tail.setPrev(self.head)
                        for i in range(2, len(iterable)):
                            temp = Node(iterable[i])
                            temp.setPrev(self.tail)
                            self.tail.setNext(temp)
                            self.tail = self.tail.getNext()

                else:
                    self.head = Node(iterable)
                    self.tail = self.head
            except:
                print('Error: if you input the parameter, it must be a nonempty list or number or string.')
    
    def getTail(self):
        return self.tail
    
    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        if self.head != None:
            self.head.setPrev(temp)
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
            if self.head != None:
                self.head.setPrev(None)
        else:
            previous.setNext(current.getNext())
            if current.getNext() != None:
                current.getNext().setPrev(previous)
    
    def append(self, item):
        temp = Node(item) 
        if self.head == None:
            self.head = temp
            self.tail = self.head
        else:
            temp.setPrev(self.tail)
            self.tail.setNext(temp)
            self.tail = temp
    def index(self, item):
        index_list = []
        current = self.head
        count = 0
        while current != None:
            if current.getData() == item:
                index_list.append(count)
            count += 1
            current = current.getNext()

        return index_list
    def pop(self):
        old_tail = self.tail
        self.tail = old_tail.getPrev()
        self.tail.setNext(None)
        return old_tail.getData()

    def insert(self, pos, item):
        temp = Node(item)
        count = 0
        previous = None
        current = self.head
        try:
            for count in range(pos+1):
                previous = current
                current = current.getNext()
            previous.setNext(temp)
            temp.setPrev(previous)
            temp.setNext(current)
            current.setPrev(temp)
        except AttributeError:
            print('ERROR: The position is out of the range of the link.')
    def __len__(self):
        temp = self.head
        count = 0
        if temp == None:
            return 0
        else:
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

            return 'A DoublyLinkedList: %s' % (','.join(str(item) for item in temp_list))
        else:
            return 'An empty DoublyLinkedList'
    def __getitem__(self, n):
            if isinstance(n, slice):
                try:
                    slice_list = []
                    if n.stop < 0 and n.start < 0:
                        i = -1
                        current = self.tail
                        while i >= n.start:
                            if i < n.stop:
                                slice_list.append(current.getData())
                            i -= 1
                            current = current.getPrev()
                        return slice_list.reverse()
                    elif n.stop >= 0 and n.start >=0:
                        i = 0
                        current = self.head
                        while i < n.stop:
                            if i >= n.start:
                                slice_list.append(current.getData())
                            i += 1
                            current = current.getNext()
                        return slice_list
                    else:
                        return 'ERROR: The start and stop of your slice must be both < 0 or >=0'

                except AttributeError:
                    return "ERROR: Your slice out of the range of link."
            elif isinstance(n, int):
                try:
                    if n < 0:
                        current = self.tail
                        i = -1
                        while i != n:
                            i -= 1
                            current = current.getPrev()
                    else:
                        current = self.head
                        i = 0
                        while i != n:
                            i += 1
                            current = current.getNext()
                    return current.getData()
                except AttributeError:
                    return 'ERROR: The position is out of the range of the link.'
            else:
                return 'ERROR: Please input a slice or an integer.'

    def __iter__(self):
        self.marker = self.head
        return self

    def __next__(self):
        while self.marker != None:
            current = self.marker
            self.marker = self.marker.getNext()
            return current
        raise StopIteration

    def __eq__(self, other):
        flag = True
        if type(self) == type(other):
            checker1 = self.head
            checker2 = other.head
            while flag and (checker1 != None) and (checker2 != None):
                if checker1.getData() != checker2.getData():
                    flag = False
                checker1 = checker1.getNext()
                checker2 = checker2.getNext()
            if flag and (checker1 == None) and (checker2 == None):
                return True
            else:
                return False

        else:
            return False
def main():
    f = [1, 2, 3, 4, 5, 6]
    g = [1, 2, 3, 4, 5]
    t = DoublyLinkedList(f)
    h = DoublyLinkedList(g)
    print(t == h)
    #for i in t:
    #    print(i.getData())
    #print(t.head.getData())
    #t.add(1)
    #t.add(2)
    #t.insert(2,2)
    #print(t)
    #print(t[-2])
    #print(t.getNext())

    return 0


if __name__ == '__main__':
    main()
