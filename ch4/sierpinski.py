#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time    : 4/6/2022 8:34 PM
@Author  : Zhaopeng SHI
@Email   : zhaopshi@gmail.com
@File    : sierpinski.py
"""


# here import the import lib
import turtle


def drawTrangle(color, points):
    t.fillcolor(color)
    t.penup()
    t.goto(points['right'])
    t.pendown()
    t.begin_fill()
    t.goto(points['left'])
    t.goto(points['top'])
    t.goto(points['right'])
    t.end_fill()


def getMid(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)


def sierpinski(degree, points):
    colormap = ['red', 'green', 'blue', 'yellow', 'pink', 'black', 'brown']
    drawTrangle(colormap[degree], points)
    if degree > 0:
        sierpinski(degree - 1,\
                   {'left':points['left'],\
                       'top':getMid(points['top'], points['left']),\
                   'right':getMid(points['left'], points['right'])})
        sierpinski(degree - 1,\
                   {'left':getMid(points['left'], points['right']),\
                       'top': getMid(points['top'], points['right']),\
                   'right': points['right']})
        sierpinski(degree - 1, \
                   {'left':getMid(points['left'], points['top']), \
                       'top' : points['top'], \
                   'right': getMid(points['top'], points['right'])})


t = turtle.Turtle()
start_points = {'right': (200, 0), 'top': (0, 200), 'left': (-200, 0)}
sierpinski(5, start_points)
turtle.done()


