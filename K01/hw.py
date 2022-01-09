#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time    : 27/12/2021 10:05 PM
@Author  : Zhaopeng SHI
@Email   : zhaopshi@gmail.com
@File    : hw.py
"""


# import package here
import timeit

lis = []


def main():
    time = []

    for n in range(10000, 10000, 100000):
        print("1")
        global lis
        lis = range(n)
        t = timeit.timeit(stmt="lis.insert(0, 1)", number=1000)
        print(t)

    return 0


if __name__ == '__main__':
    main()
