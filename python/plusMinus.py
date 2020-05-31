#!/bin/python

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
  plusTot = 0
  minTot = 0
  zerTot = 0


  _perPlus=0.0
  _perMin=0.0
  _perZero=0.0
  _len = len(arr)
  for i in range(len(arr)):
    if arr[i] < 0:
      minTot += 1
    elif arr[i] > 0:
      plusTot += 1
    else:
      zerTot += 1
      pass
  _perPlus = float(plusTot) / _len
  _perMin = float(minTot) / _len
  _perZero = float(zerTot) / _len
  _result = "{0:.6f}\n{1:.6f}\n{2:.6f}".format(_perPlus,_perMin,_perZero)

  return _result

if __name__ == '__main__':
  fptr = open(os.environ['OUTPUT_PATH'], 'w')
  n = int(raw_input())

  arr = map(int, raw_input().rstrip().split())

  plusMinus(arr)

  fptr.write(str(result) + '\n')

  fptr.close()
  #a = 0.0
  #a = 1/2
  #print a

