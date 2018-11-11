# -*- coding: utf-8 -*-

import numpy as np

def trace(diag, upper_diag, lower_diag, f):
	diag = np.array(diag)
	upper_diag = np.array(upper_diag)
	upper_diag = np.append(upper_diag,0)
	lower_diag = np.array(lower_diag)
	lower_diag = np.insert(lower_diag,0,0)
	n = len(diag)
	beta = np.zeros(n)
	x = np.zeros(n)
	y = np.zeros(n)
	
	for i in range(n):
		if i == 0:
			beta[i] = upper_diag[i]/diag[i]
			y[i] = f[i]/diag[i]
		elif i < n-1:
			beta[i] = upper_diag[i]/(diag[i] - lower_diag[i]*beta[i-1])
			y[i] = (f[i] - lower_diag[i]*y[i-1])/(diag[i] - lower_diag[i]*beta[i-1])
		else:
			y[i] = (f[i] - lower_diag[i]*y[i-1])/(diag[i] - lower_diag[i]*beta[i-1])
	for i in range(n-1,-1,-1):
		if i == n-1:
			x[i] = y[i]
		else:
			x[i] = y[i] - beta[i]*x[i+1]
	return x

if __name__ == '__main__':
	pass
