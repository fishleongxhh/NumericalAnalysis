# -*- coding: utf-8 -*-
#Author: Xu Hanhui

import numpy as np
from scipy import stats

def mc_exercise(loc, scale, size):
	print(loc, scale, size)
	x = stats.norm.rvs(loc, scale, size)
	#print(x)
	mean = sum(x)/size
	return mean

def main(loc, scale, size):
	true_mean = loc
	sample_mean = mc_exercise(loc, scale, size)
	return true_mean, sample_mean

if __name__ == '__main__':
	loc, scale, size = 0, 1, 100000
	result = main(loc, scale, size)
	print('分布的真实均值为：', result[0])
	print('样本均值为：', result[1])
