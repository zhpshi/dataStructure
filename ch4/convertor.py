#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time    : 28/1/2022 7:44 PM
@Author  : Zhaopeng SHI
@Email   : zhaopshi@gmail.com
@File    : convertor.py
"""


# import package here


def toStr(n, base):
    converString = "0123456789ABCDEF"
    if n < base:
        return converString[n]
    else:
        return toStr(n // base, base) + converString[n % base]


def main():
    print(toStr(3452, 16))
    return 0


if __name__ == '__main__':
    main()
