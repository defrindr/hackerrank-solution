#!/bin/python
import sys
#Project Euler #13: Large sum

def summing(n):
	t = 0
	for x in xrange(len(n)):
		t += n[x]
		pass
	_result = str(t)
	print _result[:10]
	pass
if __name__ == '__main__':
	_n = []
	j = int(raw_input().strip())
	for a in xrange(j):
		n = long(raw_input().strip())
		_n.append(n)
		pass
	summing(_n)
	pass