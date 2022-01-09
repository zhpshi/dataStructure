#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time    : 27/12/2021 4:09 PM
@Author  : Zhaopeng SHI
@Email   : zhaopshi@gmail.com
@File    : hw1_2.py
"""


# import package here
import time
import datetime


def main():
    f = open('pi50.4.bin', 'rb')
    dbuff = f.read()
    s = ("".join(("%02x" % d for d in dbuff))).encode()
    d1 = datetime.date(2021, 1, 1)
    found = 0
    start = time.perf_counter()
    for n in range(365):
        day = ((d1 + datetime.timedelta(days=n)).strftime("%Y%m%d")).encode()
        if day in s:
            found += 1
    end = time.perf_counter()
    print(f" The number of days is {found}. The time used is {end - start}")
    return 0


if __name__ == '__main__':
    main()
