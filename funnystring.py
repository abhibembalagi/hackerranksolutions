#!/bin/python

import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def funnyString(s):
    rs=s[::-1]
    n=len(s)
    for i in range(1,n):
        d1=abs(ord(s[i])-ord(s[i-1]))
        d2=abs(ord(rs[i])-ord(rs[i-1]))
        if d1!=d2:
            return("Not Funny")
    else:
        return"Funny" 
      

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        s = raw_input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
