#!/bin/python

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    length=len(arr)
    sum=0
    for i in range(length):
        sum=sum+arr[i]
    print( sum-max(arr),sum-min(arr))
if __name__ == '__main__':
    arr = map(int, raw_input().rstrip().split())

    miniMaxSum(arr)
