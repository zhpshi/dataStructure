#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time    : 26/1/2022 1:44 PM
@Author  : Zhaopeng SHI
@Email   : zhaopshi@gmail.com
@File    : h02.py
"""
# import package here
"""

"""
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

def expressionConvert(expression):
    opstack = Stack()
    prec = {}
    prec["^"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    postfixlist = []
    tokenList = list(expression)
    s = list(expression)
    for item in tokenList:
        if item in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T","U", "V", "W", "X", "Y", "Z"] \
                or item in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            postfixlist.append(item)
        else:
            if item =="(" or opstack == []:
                opstack.push(item)
            elif item == ")":
                top = opstack.pop()
                while top != "(" and top != None:
                    postfixlist.append(top)
                    top = opstack.pop()
            else:
                while (not opstack.isEmpty()) and (prec[opstack.peek()] >= prec[item]):
                    postfixlist.append(opstack.pop())
                opstack.push(item)
    while not opstack.isEmpty():
        postfixlist.append(opstack.pop())
    return "%s" %("".join(s for s in postfixlist))


def calExpression(a):
    expression_list = list(a)
    num_stack = Stack()
    for item in expression_list:
        if item in "1234567890":
            num_stack.push(float(item))
        elif item == "+":
            num = num_stack.pop()
            num_stack.push(num_stack.pop() + num)
        elif item == "-":
            num = num_stack.pop()
            num_stack.push(num_stack.pop() - num)
        elif item == "*":
            num = num_stack.pop()
            num_stack.push(num_stack.pop() * num)
        elif item == "/":
            num = num_stack.pop()
            num_stack.push(num_stack.pop() / num)
        elif item == "^":
            num = num_stack.pop()
            num_stack.push(num_stack.pop() ** num)
        print(str(num_stack))
    return num_stack.pop()


def main():
    a = "(5+2)+4*3^2+1"
    b = expressionConvert(a)
    print(b)
    print(calExpression(b))
    return 0


if __name__ == '__main__':
    main()
