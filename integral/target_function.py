# -*- coding: utf-8 -*-
import math

def target_function(x):
	x = float(x)
	if x == 0:
		return 1
	else:
		return math.sin(x)/x

if __name__ == '__main__':
	pass
