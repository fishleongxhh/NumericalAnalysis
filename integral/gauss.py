# -*- coding: utf-8 -*-

import numpy as np
from target_function import target_function

def get_nodes(start, end, num):
	if num == 3:
		A = [0.5555556, 0.8888889, 0.5555556]
		nodes = [-0.7745967, 0.0, 0.7745967]
	elif num == 4:
		A = [0.3478548, 0.6521452, 0.6521452, 0.3478548]
		nodes = [-0.8611363, -0.3399810, 0.3399810, 0.8611363]
	else:
		A = []
		nodes = []
	return np.array(A), np.array(nodes)

def gauss(start, end, num):
	if num not in (3,4):
		print("The number of nodes should be 3 or 4!")
		return None
	A, nodes = get_nodes(start, end ,num)
	nodes = nodes*(end - start)/2 + (start + end)/2
	f = [target_function(i) for i in nodes]
	integral = (end - start)/2 * np.dot(A, f)
	return integral

if __name__ == '__main__':
	pass
