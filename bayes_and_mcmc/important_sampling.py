# -*- coding: utf-8 -*-
#Author: Xu Hanhui

import math
import numpy as np
from scipy import stats
import matplotlib  
matplotlib.use('Agg') 
import matplotlib.pyplot as plt

def imp_samp_exercise(size=1000):
	df = 3
	loc, scale = 0, 1
	sample = stats.t.rvs(df, loc, scale, size)
	norm_density_value = [stats.norm.pdf(i, loc, scale) for i in sample]
	t_density_value = [stats.t.pdf(i, df, loc, scale) for i in sample]
	weight = [norm_density_value[i]/t_density_value[i] for i in range(len(sample))]
	sample_2 = [i**2 for i in sample]

	expect_hat = np.dot(sample, weight)/size
	var_hat = np.dot(sample_2, weight)/size - expect_hat**2
	#绘制出weight的直方图
	#plt.hist(weight, 50, normed=1, facecolor='green', alpha=0.3, label="weight")
	plt.title('Hist for weight of t approximate norm')
	plt.savefig('./Hist_for_weight_of_t_approximate_norm.png', format='png', dpi=600)
	plt.close()
	print("估计的正态分布均值为：", expect_hat)
	print("真实的正态分布均值为：", loc)
	print("估计的正态分布方差为：", var_hat)
	print("真实的正态分布方差为：", scale**2)

def imp_samp_exercise2(size=1000):
	df = 3
	loc, scale = 0, 1
	sample = stats.norm.rvs(loc, scale, size)
	norm_density_value = [stats.norm.pdf(i, loc, scale) for i in sample]
	t_density_value = [stats.t.pdf(i, df, loc, scale) for i in sample]
	weight = [t_density_value[i]/norm_density_value[i] for i in range(len(sample))]
	sample_2 = [i**2 for i in sample]

	expect_hat = np.dot(sample, weight)/size
	var_hat = np.dot(sample_2, weight)/size - expect_hat**2
	#绘制出weight的直方图
	#plt.hist(weight, 50, normed=1, facecolor='green', alpha=0.3, label="weight")
	plt.title('Hist for weight of norm approximate t')
	plt.savefig('./Hist_for_weight_of_norm_approximate_t.png', format='png', dpi=600)
	plt.close()
	print("估计的t(3)均值为：", expect_hat)
	print("真实的t(3)均值为：", loc)
	print("估计的t(3)方差为：", var_hat)
	print("真实的t(3)方差为：", df/(df-2))


if __name__ == "__main__":
	#绘制标准正态分布和t(3)分布的密度函数
	x = np.linspace(-5,5,500)
	y_t = stats.t.pdf(x, df=3, loc=0, scale=1)
	y_norm = stats.norm.pdf(x, loc=0, scale=1)
	plt.plot(x,y_t,'ro-',linewidth=1.0,markersize=1,label='t')
	plt.plot(x,y_norm,'ko-',linewidth=1.0,markersize=1,label='norm')
	plt.title("normal distribution vs t distibution")
	plt.legend(loc='best')
	plt.savefig('./normal_dist_vs_t_dist.png', format='png', dpi=600)
	plt.close()
	#估计正态分布和t(3)的期望和方差
	imp_samp_exercise(size=1000)
	print("\n")
	imp_samp_exercise2(size=1000)
	#绘制x^2*N(0,1)/t(3)和x^2*t(3)/N(0,1)函数
	x = np.linspace(-10,10, 1000)
	norm_dist = stats.norm.pdf(x, 0, 1)
	t_dist = stats.t.pdf(x,3,0,1)
	#plt.plot(x, x*norm_dist/t_dist,label='x*norm_dist/t_dist')
	plt.plot(x, x*t_dist/norm_dist,label='x*t_dist/norm_dist')
	plt.title('x*N(0,1)/t(3) and x*t(3)/N(0,1)')
	plt.legend(loc='best')
	plt.savefig('./imp3.png',format='png',dpi=600)
	plt.close()
	#plt.plot(x, [i**2 for i in x]*norm_dist/t_dist,label='x^2*norm_dist/t_dist')
	plt.plot(x, [i**2 for i in x]*t_dist/norm_dist,label='x^2*t_dist/norm_dist')
	plt.title("x^2*N(0,1)/t(3) and x^2*t(3)/N(0,1)")
	plt.legend(loc='best')
	plt.savefig('./imp4.png',format='png',dpi=600)
	plt.close()
