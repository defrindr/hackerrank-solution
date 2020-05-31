#!/bin/python 
#defri indra m
#dec 24 2018

def convert(_t):
	__t = _t[-2:] #am/pm
	___t = _t[:2] # jam
	____t = _t[2:8]

	if __t == "AM":
		if ___t == "12":
			___t = "00"
	elif __t == "PM":
		if ___t != "12":
			___t = str(int(___t)+12)

	_____t = ___t+____t
	return _____t


if __name__ == '__main__' :
	t_ = raw_input()
	______t = convert(t_)
	print ______t