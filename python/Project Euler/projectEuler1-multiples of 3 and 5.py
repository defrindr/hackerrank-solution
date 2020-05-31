#!/bin/python


#Project Euler #1: Multiples of 3 and 5
# Defri Indra M

import sys

_n = []

t = int(raw_input().strip())
for jumlah in range(t):
    n = int(raw_input().strip())
    _n.append(n)
for a in xrange(len(_n)):
	_tmp = 0
	for i in xrange(_n[a]):
		if i % 3 == 0 :
			_tmp += i
		elif i % 5 == 0:
			_tmp += i
		else:
			_tmp += 0
			pass
	print _tmp
