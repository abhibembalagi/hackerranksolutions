#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_count=len(apples)
    orange_count=len(oranges)
    acount=0
    ocount=0
    for i in range(apple_count):
        temp=a+apples[i]
        if (temp in range(s,t+1)):
            acount=acount+1
    for i in range(orange_count):
        temp=b+oranges[i]
        if (temp in range(s,t+1)):
            ocount=ocount+1
    print(acount)
    print(ocount)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
