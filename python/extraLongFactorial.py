#!/bin/python
#Defri Indra M
def soLong(n):
	_result=1
	while n >= 1:
		_result*=n
		n-=1
	print _result

num = int(raw_input())
soLong(num)