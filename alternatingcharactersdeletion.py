#!/bin/python

import math
import os
import random
import re
import sys

t=input()
for _ in range(t):
    s=raw_input()
    delete_cnt=0
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            delete_cnt+=1
    print delete_cnt 
