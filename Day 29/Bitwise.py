#!/bin/python3

import math
import os
import random
import re
import sys

def f_m_bitwise(n, k):
    m_bitwise = 0
    for i in range(1, n + 1):
        for j in range(1, i):
            bitwise = i & j
            if m_bitwise < bitwise < k:
                m_bitwise = bitwise
                if m_bitwise == k - 1:
                    return m_bitwise


    return m_bitwise

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        print(f_m_bitwise(n, k))
