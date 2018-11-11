# -*- coding: utf-8 -*-

import numpy as np
import warnings
import sys
import copy

def locate(x, new_x):
	n = len(x)
	if new_x < x[0] or new_x > x[-1]:
		print('new_x is out of range!')
		return
	for i in range(n):
		if x[i] > new_x:
			return (x[i-1],x[i])
	return (x[-2],x[-1])

def predict(x, my_dict, new_x):
	loc = locate(x, new_x)
	x0, x1 = loc[0], loc[1]
	f0, f1 = my_dict[x0], my_dict[x1]
	return (new_x-x1)/(x0-x1)*f0 + (new_x-x0)/(x1-x0)*f1

def piecewise_linear_interpolation(x, y, new_x, sort=True):
	if not isinstance(x,list):
		print('Type of input x should be list!')
		return
	if not isinstance(y,list):
		print('Type of input y should be list!')
		return
	if len(x) != len(y):
		print('The length of x and y should be equal!')
		return
	if len(x) <=1:
		print('The lenth of x and y should be larger than 1!')
		return
	if not (isinstance(new_x, list) or isinstance(new_x, tuple)):
		try:
			new_x = list(new_x)
		except:
			print('The type of input new_x is illegal!')
			return
	#将x和y整合成一个字典
	my_dict = dict(zip(x,y))
	#如果x不是递增的，则需要进行排序
	if sort:
		x = sorted(x)
	#利用分段线性插值预测new_x处的函数值
	new_y = [predict(x, my_dict, e) for e in new_x]
	return new_y

if __name__ == '__main__':
	pass
