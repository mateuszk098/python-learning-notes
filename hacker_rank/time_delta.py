#!/bin/python3

"""
See description at https://www.hackerrank.com/challenges/python-time-delta
"""

import math
import os
import random
import re
import sys

from datetime import datetime


def time_delta(t1, t2):
    t1_dt = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    t2_dt = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
    return str(int(abs((t1_dt - t2_dt).total_seconds())))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        fptr.write(delta + '\n')
    fptr.close()
