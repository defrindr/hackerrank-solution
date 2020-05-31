#!/bin/python
#Project Euler #6: Sum square difference

import sys

def ssd(n):
	num1 = 0
	num2 = 0
	_result = 0

	for x in xrange(1,n+1):
		num1 += x
		num2 += x**2
	num1= num1**2

	_result = num1-num2
	print _result

n = []
t = int(raw_input().strip())
for a0 in xrange(t):
    n.append(int(raw_input().strip()))
for x in xrange(len(n)):
	ssd(n[x])