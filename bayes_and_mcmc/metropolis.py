# -*- coding: utf-8 -*-
#Author: Xu Hanhui

import numpy as np
from scipy.stats import multivariate_normal, uniform
import matplotlib  
matplotlib.use('Agg') 
import matplotlib.pyplot as plt 

def metropolis_exercise(start_point=[0,0],num=1000, sigma=0.2):
	all_points = [start_point]
	target_mean = [0,0]
	target_cov = [[1,0], [0,1]]
	proposal_cov = [[sigma**2,0], [0, sigma**2]]
	last_accept = start_point
	refuse_cnt = 0
	for j in range(1,num):
		proposal_mean = all_points[j-1]
		proposal_point = multivariate_normal.rvs(mean=proposal_mean, cov=proposal_cov)
		p1 = multivariate_normal.pdf(proposal_point, target_mean, target_cov)
		p2 = multivariate_normal.pdf(last_accept, target_mean, target_cov)
		ratio = p1/p2
		if uniform.rvs(0,1) < ratio:
			all_points.append(proposal_point)
			last_accept = proposal_point
		else:
			all_points.append(last_accept)
			refuse_cnt += 1
	print(refuse_cnt/float(num))
	return all_points

def main():
	start_points = [[0,0], [-2.5,-2.5], [-2.5,2.5], [2.5,-2.5], [2.5,2.5]]
	chains = []
	for point in start_points:
		new_chain = metropolis_exercise(point, 5000, 0.2)
		chains.append(new_chain)
	return chains

if __name__ == '__main__':
	chains = main()
	#print(chains)
	line_types = ['ro-','bo-','yo-','ko-','co-']
	for j in range(len(chains)):
		x = [i[0] for i in chains[j]]
		y = [i[1] for i in chains[j]]
		plt.plot(x,y,line_types[j],linewidth=1.0,markersize=1,label = str(j))
	plt.title('Five independent Markov simulation chains')
	plt.xlabel('theta[0]')
	plt.ylabel('theta[1]')
	plt.legend(loc='best')
	plt.savefig('./mcmc_chains_5000steps.png', format='png', dpi=600)
	plt.close()

	#扔去前半段，只保留链的后半段，绘制散点图
	x = []
	y = []
	for j in range(len(chains)):
		tmp_x = [i[0] for i in chains[j]]
		tmp_y = [i[1] for i in chains[j]]
		start = int(len(tmp_x)/2)
		x.extend(tmp_x[:])
		y.extend(tmp_y[:])
	plt.scatter(x,y,s=5)
	plt.title('Markov simulation for N(0,I)')
	plt.xlabel('theta[0]')
	plt.ylabel('theta[1]')
	plt.savefig('./mcmc_scatter.png', format='png', dpi=600)
	plt.close()

	#绘制每个随机变量采样的直方图
	num_bins = 50
	plt.hist(x, num_bins, normed=1, facecolor='green', alpha=0.3, label="theta[0]")
	plt.title('Hist for theta[0]')
	plt.legend()
	plt.savefig('./theta0_hist.png', format='png', dpi=600)
	plt.close()

	plt.hist(y, num_bins, normed=1, facecolor='purple', alpha=0.3, label="theta[1]")
	plt.title('Hist for theta[1]')
	plt.legend()
	plt.savefig('./theta1_hist.png', format='png', dpi=600)
	plt.close()
