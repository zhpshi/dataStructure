#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time    : 27/12/2021 9:41 PM
@Author  : Zhaopeng SHI
@Email   : zhaopshi@gmail.com
@File    : bigo.py
"""


# import package here
from big_o import big_o, datagen


def main():
    best, others = big_o(
        sorted,
        lambda n: datagen.integers(n, 10000, 50000),
        min_n=10000,
        max_n=100000,
        n_measures=100,
    )
    print(best)
    return 0


if __name__ == '__main__':
    main()
