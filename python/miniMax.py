#!/bin/python

def MM(n):
	_min= 0
	_max=0
	n.sort()
	for a in xrange(1,len(n)):
		_max+=n[a]
	for x in xrange(0,len(n)-1):
		_min+=n[x]
	print "{} {}".format(_min,_max)
n = map(int,raw_input().rstrip().split())
MM(n)
