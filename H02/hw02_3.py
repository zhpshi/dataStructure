#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time    : 26/1/2022 11:28 PM
@Author  : Zhaopeng SHI
@Email   : zhaopshi@gmail.com
@File    : hw02_3.py
"""
# ======= 3 HTML标记匹配 =======
# 实现扩展括号匹配算法，用来检查HTML文档的标记是否匹配。
# HTML标记应该成对、嵌套出现，
# 开标记是<tag>这种形式，闭标记是</tag>这种形式。
#
# 创建一个函数，接受参数为一个字符串，为一个HTML文档中的内容，
# 返回True或False，表示该字符串中的标记是否匹配。
# 输入样例1：
# <html> <head> <title> Example </title> </head> <body> <h1>Hello, world</h1> </body> </html>
# 输出样例1：
# True
# 输入样例2：
# <html> <head> <title> Test </title> </head> <body> <p>It's just a test.</p> <p>And this is for False.<p> </body> </html>
# 输出样例2：
# False

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
                if tag_stack.isEmpty():
                    isOK = False
                else:
                    if isMatch(tag_stack.peek(), tag):
                        tag_stack.pop()
                    else:
                        isOK = False
            i = index + 1
        else:
            i += 1
        #print(tag)
        #print(index)


    if isOK and tag_stack.isEmpty():
        return True
    else:
        return False





def main():
    s1 = '<html> <head> <title> Example </title> </head> <body> <h1>Hello, world</h1> </body> </html>'
    s2 = "<html> <head> <title> Test </title> </head> <body> <p>It's just a test.</p> <p>And this is for False.<p> </body> </html>"
    print(htmlmatch(s1))
    print("#############################")
    print(htmlmatch(s2))
    return 0


if __name__ == '__main__':
    main()
