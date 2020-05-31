#!/bin/python

#Project Euler #10: Summation of primes 

import sys
def bilPrim(n):
	out = []
	_result = 0
	sieve = [True] * (n+1)
	for p in range(2, n+1):
		if (sieve[p]):
			out.append(p)
			for i in range(p, n+1, p):
				sieve[i] = False
	for w in xrange(len(out)):
		_result += out[w]
	print _result



_n = []
t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    _n.append(n)
for x in xrange(len(_n)):
	bilPrim(_n[x])