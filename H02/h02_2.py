#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time    : 26/1/2022 10:15 PM
@Author  : Zhaopeng SHI
@Email   : zhaopshi@gmail.com
@File    : h02_2.py
"""


# import package here
# ======= 2 基数排序 =======
# 实现一个基数排序算法，用于10进制的正整数从小到大的排序。
#
# 思路是保持10个队列(队列0、队列1......队列9、队列main)，开始，所有的数都在main队列，没有排序。
# 第一趟将所有的数根据其10进制个位(0~9)，放入相应的队列0~9，全放好后，按照FIFO的顺序，将每个队列的数合并排到main队列。
# 第二趟再从main队列队首取数，根据其十位的数值，放入相应队列0~9，全放好后，仍然按照FIFO的顺序，将每个队列的数合并排到main队列。
# 第三趟放百位，再合并；第四趟放千位，再合并。
# 直到最多的位数放完，合并完，这样main队列里就是排好序的数列了。
#
# 创建一个函数，接受参数为一个列表，为需要排序的一系列正整数，
# 返回排序后的数字列表。
# 输入样例1：
# [1, 2, 4, 3, 5]
# 输出样例1：
# [1, 2, 3, 4, 5]
# 输入样例2：
# [8, 91, 34, 22, 65, 30, 4, 55, 18]
# 输出样例2：
# [4, 8, 18, 22, 30, 34, 55, 65, 91]

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
