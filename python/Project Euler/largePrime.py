 #!/bin/python
# Project Euler #3: Largest prime factor
# Defri Indra M
import sys


def ajaib(n):
	_tmp = []
	loop = 2
	while loop <= n:
		if n % loop == 0 :
			n /= loop
			_tmp.append(loop)
		else:
			loop += 1

	_tmp.sort()
	_tmp.reverse()
	result = _tmp[0]

	return result


_input = []

t = int(raw_input().strip())
for jumlah in range(t):
    n = long(raw_input().strip())
    _input.append(n)
for i in range(len(_input)):
	a = ajaib(_input[i])
	print a