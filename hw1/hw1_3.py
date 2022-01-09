#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time    : 27/12/2021 5:04 PM
@Author  : Zhaopeng SHI
@Email   : zhaopshi@gmail.com
@File    : hw1_3.py
"""


# import package here
import time
import datetime


def main():
    f = open("pi50.4.bin", "rb")
    dbuff = f.read()
    s = ("".join(('%02x' % d for d in dbuff))).encode()
    start = time.perf_counter()
    d1 = datetime.date(2021, 1, 1)
    days = {
        ((d1 + datetime.timedelta(days=n)).strftime("%m%d")).encode()
        for n in range(365)
    }
    y = b"2021"
    found = 0
    idx = s.find(y)
    while idx >= 0:
        p4 = s[idx + 4 : idx + 8]
        if p4 in days:
            found += 1
            days.remove(p4)
        idx = s.find(y, idx + 4)

    end = time.perf_counter()

    print(f"The number is {found}. The time used is {end - start}")
    return 0


if __name__ == '__main__':
    main()
