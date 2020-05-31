#!/bin/python

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    _result=0
    _sum1=0
    _sum2=0
    for a in range(len(arr)):
        _sum1+=int(arr[a][a])
        _sum2+=int(arr[a][(len(arr)-1)-a])
    
    _result = _sum1-_sum2

    if _result < 0:
        _result*= -1
    return _result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    arr = []

    for _ in xrange(n):
        arr.append(map(int, raw_input().rstrip().split()))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

