#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time    : 26/12/2021 4:43 PM
@Author  : Zhaopeng SHI
@Email   : zhaopshi@gmail.com
@File    : timeit_test.py
"""


# import package here
from timeit import Timer
import numpy as np

lst = list(range(1000000))


def test1():
    global lst
    lst.pop(0)


def main():
    t1 = Timer("test1()", "from __main__ import test1")

    print(f"{t1.timeit(number=1000):.3f} seconds")
    return 0


if __name__ == '__main__':

    main()
