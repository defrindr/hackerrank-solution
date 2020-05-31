#!/bin/python

#Project Euler #10: Summation of primes
#defri indra m
import sys

def summing(a):
	for b in a:
		n= b+1
		sum, sieve = 0, [True] * n
		for p in range(2, n):
			if sieve[p]:
				sum += p
				for i in range(p*p, n, p):
					sieve[i] = False
		print sum


_n = []
t = int(raw_input().strip())
for a0 in xrange(t):
	n = int(raw_input().strip())
	_n.append(n)
summing(_n)
