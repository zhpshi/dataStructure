import numpy as np

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

def hotPotato(namelist, num):

    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(1, num):
            head = simqueue.dequeue()
            simqueue.enqueue(head)

        simqueue.dequeue()
    
    return simqueue.dequeue()
def main():
    print(hotPotato(["A" , "B" , "C" , "D" , "E" , "F"], 3))
    return 0

if __name__ == '__main__':
    main()
