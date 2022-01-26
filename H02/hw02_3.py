#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time    : 26/1/2022 11:28 PM
@Author  : Zhaopeng SHI
@Email   : zhaopshi@gmail.com
@File    : hw02_3.py
"""


# import package here
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
    def __str__(self):
        return "%s" % (','.join(str(i) for i in self.items))
def htmlmatch(expression):
    def isOpen(tag):
        return not tag[1] == '/'
    def isMatch(open, close):
        return open == close.replace("/", "")
    def getTag(string, index):
        tag = ""
        while string[index] != '>':
            tag += string[index]
            index += 1
        tag += ">"
        return tag, index

    tag_stack = Stack()
    isOK = True
    i = 0
    while isOK and i < len(expression):
        if expression[i] == '<':
            tag, index = getTag(expression, i)
            if isOpen(tag):
                tag_stack.push(tag)
            else:



def main():
    return 0


if __name__ == '__main__':
    main()
