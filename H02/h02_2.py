#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time    : 26/1/2022 10:15 PM
@Author  : Zhaopeng SHI
@Email   : zhaopshi@gmail.com
@File    : h02_2.py
"""


# import package here

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
    def __str__(self):
        return "%s" % (','.join(str(i) for i in self.items))
def sort(num_list):
    main_queue = Queue()
    maximum = max(num_list)
    n = len(str(maximum))
    final_list = []
    for s in num_list:
        main_queue.enqueue(s)
    queue_list = []
    for i in range(10):
        queue_list.append(Queue())
    for i in range(n):
        visual_list = []
        while not main_queue.isEmpty():
            item = main_queue.dequeue()
            if len(str(item)) < i+1:
                queue_list[0].enqueue(item)
            else:
                queue_list[int(str(item)[i])].enqueue(item)
        for i in range(10):
            while not queue_list[i].isEmpty():
                s = queue_list[i].dequeue()
                main_queue.enqueue(s)
                visual_list.append(s)
        print(visual_list)
    while not main_queue.isEmpty():
        final_list.append(main_queue.dequeue())
    return final_list


def main():
    a = [2, 225, 25, 36, 12, 99, 2, 1, 5, 5563, 12251]
    print(sort(a))
    return 0


if __name__ == '__main__':
    main()
