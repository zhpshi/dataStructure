#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2021/12/19 20:05:04
@Author  : Zhaopeng SHI
@Email   : zhaopshi@gmail.com
@File    : hw1.py

"""

# here put the import lib
import timeit
import os


def main():

    f = open('pi50.4.bin', 'rb')
    d_buff = f.read()
    s = ''.join(('%02x' % d for d in d_buff))
    print(s)
    return 0

if __name__ == '__main__':
    main()
