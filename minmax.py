#!/bin/python
#!/bin/python

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    min_ele=sys.maxint
    max_ele=0
    arr_sum=0
    for val in arr:
        min_ele=min(min_ele,val)
        max_ele=max(max_ele,val)
        arr_sum+=val
    return arr_sum-max_ele,arr_sum-min_ele
if __name__=='__main__':
    arr=map(int,raw_input().rstrip().split())
    print" ".join(map(str,miniMaxSum(arr)))
