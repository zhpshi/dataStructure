#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time    : 3/6/2022 10:49 PM
@Author  : Zhaopeng SHI
@Email   : zhaopshi@gmail.com
@File    : turtle_plot.py
"""


# here import the import lib
import turtle

def drawSpiral(t, line_lenght):
    if line_lenght > 0:
        t.forward(line_lenght)
        t.right(90)
        drawSpiral(t, line_lenght-5)


def tree(t, line_length):
    if line_length > 5:
        t.forward(line_length)
        t.right(20)
        tree(t, line_length - 15)
        t.left(40)
        tree(t, line_length - 15)
        t.right(20)
        t.backward(line_length)


def main():
    t = turtle.Turtle()
    t.left(90)
    t.penup()
    t.backward(100)
    t.pendown()
    t.pensize(2)
    t.pencolor('green')
    tree(t, 80)
    turtle.done()

    return 0


if __name__ == "__main__":
    main()
