# -*- coding: utf-8 -*-

import numpy as np
from target_function import target_function

def get_nodes(start, end, num):
	x = np.linspace(start, end, num+1)
	return x

def compound_trapezoid(start, end, num):
	start = float(start)
	end = float(end)
	num = int(num)
	nodes = get_nodes(start, end, num)
	f = [2*target_function(i) for i in nodes]
	f[0] = f[0]/2
	f[-1] = f[-1]/2
	step = (end - start)/num
	return step/2*sum(f)

if __name__ == '__main__':
	pass
