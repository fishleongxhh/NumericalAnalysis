# -*- coding: utf-8 -*-

import numpy as np
from target_function import target_function

def expand_nodes(nodes):
	n = len(nodes)
	new_nodes = [(nodes[i]+nodes[i+1])/2 for i in range(n-1)]
	nodes = sorted(nodes + new_nodes)
	return new_nodes, nodes

def romberg(start, end, k=4, ep=1e-5, choose_k=True, max_k=10):
	if choose_k:
		t_mat = np.zeros((k,k))
	else:
		t_mat = np.zeros((max_k,max_k))
	p = t_mat.shape[0]
	nodes = [start, end]
	h = (end - start)
	t_mat[0,0] = (target_function(start) + target_function(end))*h/2
	for k in range(1,p):
		new_nodes, nodes = expand_nodes(nodes)
		t_mat[k,0] = t_mat[k-1,0]/2 + sum([target_function(i) for i in new_nodes])*h/2
		for j in range(1,k+1):
			t_mat[k,j] = (1+1/(4**j-1))*t_mat[k,j-1] - 1/(4**j-1)*t_mat[k-1,j-1]
		if choose_k and (k == 4):
			break
		if k == max_k:
			break
		if (not choose_k) and abs(t_mat[k,k]-t_mat[k-1,k-1])<ep:
			break
		h = h/2
	integral = t_mat[k,k]
	print(t_mat)
	return integral

if __name__ == '__main__':
	pass


