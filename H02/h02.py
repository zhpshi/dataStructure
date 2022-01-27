#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time    : 26/1/2022 1:44 PM
@Author  : Zhaopeng SHI
@Email   : zhaopshi@gmail.com
@File    : h02.py
"""
# import package here
# ======= 1 中缀表达式求值 =======
# 通过把“中缀转后缀”和“后缀求值”两个算法功能集成在一起（非简单的顺序调用），
# 实现对中缀表达式直接求值，新算法还是从左到右扫描中缀表达式，
# 但同时使用两个栈，一个暂存操作符，一个暂存操作数，来进行求值。
#
# 创建一个函数，接受参数为一个字符串，即一个中缀表达式，
# 其中每个数字或符号间由一个空格隔开；
# 返回一个浮点数，即求值的结果。（支持 + - * / ^ 五种运算）
#   其中“ / ”定义为真除True DIV，结果是浮点数类型
# 输入样例1：
# ( 2 + 3 ) * 6 + 4 / 2
# 输出样例1：
# 32.0
# 输入样例2：
# 2 ^ 3 + 4 * 5 - 16 / 2
# 输出样例2：
# 20.0
# 输入样例3：
# ( 5 + 1 ) * 2 / 3 - 3 ^ ( 2 + 8 / 4 ) / 9 + 6
# 输出样例3：
# 1.0
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
