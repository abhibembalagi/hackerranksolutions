#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    max_count=0
    min_count=0
    max_no=scores[0]
    min_no=scores[0]
    for i in range(len(scores)):
        if scores[i]>max_no:
            max_no=scores[i]
            max_count+=1
        elif scores[i]<min_no:
            min_no=scores[i]
            min_count+=1
    return[max_count,min_count]

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)
    print (result)
    '''fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
'''
