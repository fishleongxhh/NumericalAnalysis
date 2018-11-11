# -*- coding: utf-8 -*-

import numpy as np
from trace import trace

def locate(x, new_x):
    n = len(x)
    if new_x < x[0] or new_x > x[-1]:
        print('new_x is out of range!')
        return
    for i in range(n):
        if x[i] > new_x:
            return (i-1,i)
    return (n-2, n-1)

def predict(x, y, h, M, new_x):
	loc = locate(x, new_x)
	j = loc[0]
	a = M[j]*((x[j+1]-new_x)**3)/(6*h[j])
	b = M[j+1]*((new_x-x[j])**3)/(6*h[j])
	c = (y[j]-M[j]/6*h[j]**2)*(x[j+1]-new_x)/h[j]
	d = (y[j+1]-M[j+1]/6*h[j]**2)*(new_x-x[j])/h[j]
	return a+b+c+d

def spline3(x, y, new_x, boundary, boundary_type='second_derivative', sort=True):
	if boundary_type not in ('derivative', 'second_derivative'):
		print('boundary_type can noly be "derivative" or "second_derivative!"')
		return
	if len(boundary) != 2:
		print('The length of boundary can only be 2!')
		return
	if not (isinstance(new_x,list) or isinstance(new_x,tuple)):
		try:
			new_x = [new_x]
		except:
			print('The type of new_x is illegal! new_x should be a list or tuple!')
			return
	if sort:
		my_dict = dict(zip(x,y))
		x = sorted(x)
		y = [my_dict[i] for i in x]
	x = np.array(x)
	y = np.array(y)
	n = len(x)
	boundary = np.array(boundary)
	#每个区间长度
	h = x[1:] - x[:-1]
	#miu为三对角矩阵的下次对角，lamb为上次对角, d为三对角方程右边的y向量
	miu = h[:-1]/(h[:-1]+h[1:])
	lamb = h[1:]/(h[1:]+h[:-1])
	d = 6* ((y[2:]-y[1:-1])/(x[2:]-x[1:-1]) - (y[1:-1]-y[:-2])/(x[1:-1]-x[:-2])) / (h[:-1]+h[1:])
	#根据边界条件的不同调整miu, lamb, d的两侧
	if boundary_type == 'derivative':
		lamb = np.insert(lamb, 0, 1)
		miu = np.append(miu, 1)
		d = np.insert(d,[0,len(d)],[6*((y[1]-y[0])/(x[1]-x[0])-boundary[0])/h[0], 6*(boundary[1]-(y[-1]-y[-2])/(x[-1]-x[-2]))/h[-1]])
	else:
		lamb = np.insert(lamb, 0, 0)
		miu = np.append(miu, 0)
		d = np.insert(d, [0,len(d)], [2*boundary[0], 2*boundary[1]])
	#求解三对角方程得到中间量M
	M = trace(np.array([2]*n), lamb, miu, d)
	#预测
	new_y = [predict(x,y,h,M,e) for e in new_x]
	return new_y

if __name__ == '__main__':
	pass
