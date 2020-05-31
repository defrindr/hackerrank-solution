#!/bin/python

import math
import os
import random
import re
import sys

def timeInWords(h, m):
	h_ = ['one','two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']
	m_ = ['o\' clock','one','two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve','thirteen','fourteen','quarter','sixteen','seventeen','eighteen','nineteen', 'twenty','twenty one','twenty two','twenty three','twenty four','twenty five','twenty six','twenty seven','twenty eight','twenty nine','half']
	m__ = 0
	if 0 < m < 30:
		if m == 1:
			_result = m_[m]+" minute past "+h_[h-1]
		elif 1 < m < 15:
			_result = m_[m]+" minutes past "+h_[h-1]
		elif 15 < m < 30:
			_result = m_[m]+" minutes past "+h_[h-1]
		elif m == 15:
			_result = m_[m]+" past "+h_[h-1]
	elif m == 30:
		_result = m_[m]+" past "+h_[h-1]
	elif m == 0 :
		_result = h_[h-1]+" "+ m_[m]
	elif 30 < m < 60:
		m__ = 60 - m
		if m__ < 15:
			_result = m_[m__]+" minutes to "+h_[h]
		elif 15 < m__ < 30:
			_result = m_[m__]+" minutes to "+h_[h]
		elif m__ == 15:
			_result = m_[m__]+" to "+h_[h]

	return _result 

if __name__ == '__main__':
	# Hour Input
	h = int(input())
	# Minute Input
	m = int(input())
	result = timeInWords(h, m)
	print(result)