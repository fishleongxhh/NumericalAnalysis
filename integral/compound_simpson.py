# -*- coding: utf-8 -*-

import numpy as np
from target_function import target_function

def get_nodes(start, end, num):
	step = (end - start)/num
	nodes1 = np.linspace(start, end, num+1)
	nodes2 = [i+step/2 for i in nodes1[:-1]]
	return nodes1, nodes2

def compound_simpson(start, end, num):
	nodes1, nodes2 = get_nodes(start, end ,num)
	f1 = [2*target_function(i) for i in nodes1]
	f1[0] /= 2
	f1[-1] /= 2
	f2 = [4*target_function(i) for i in nodes2]
	step = (end - start)/num
	return step/6*(sum(f1)+sum(f2))

if __name__ == '__main__':
	pass
