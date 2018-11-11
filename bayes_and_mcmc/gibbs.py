# -*- coding: utf-8 -*-
#Author: Xu Hanhui

import numpy as np
from scipy.stats import norm
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def gibbs_exercise(start_point=[0,0], num=1000, rho=0.8):
	all_points = [start_point]
	#print(start_point)
	target_mean = [0,0]
	target_cov = [[1,rho], [rho,1]]
	last_accept = start_point[:]
	proposal_var = 1 - rho**2
	for j in range(1,num):
		for k in [0,1]:
			proposal_mean = target_mean[k] + rho*(last_accept[1-k] - target_mean[1-k])
			last_accept[k] = norm.rvs(proposal_mean, proposal_var)
			#print(last_accept)
			all_points.append(last_accept[:]) #注意，此处必须要加[:]切片索引！！
	#print(all_points[0])
	return all_points

if __name__ == '__main__':
    start_points = [[-2.5,-2.5], [-2.5,2.5], [2.5,-2.5], [2.5,2.5]]
    chains = []
    for point in start_points:
        new_chain = gibbs_exercise(point, 2000, 0.8)
        chains.append(new_chain)
    #print(chains)
    line_types = ['ro-','yo-','ko-','co-']
    for j in range(len(chains)):
        x = [i[0] for i in chains[j]]
        y = [i[1] for i in chains[j]]
        print([x[0],y[0]])
        plt.plot(x,y,line_types[j],linewidth=1.0,markersize=1,label = str(j))
    plt.title('Four independent Gibbs simulation chains')
    plt.xlabel('theta[0]')
    plt.ylabel('theta[1]')
    plt.legend(loc='best')
    plt.savefig('./gibbs_sampling_2000steps.png', format='png', dpi=600)
    plt.close()

	#扔去前半段，只保留链的后半段，绘制散点图
    for j in range(len(chains)):
        x = [i[0] for i in chains[j]]
        y = [i[1] for i in chains[j]]
        start = int(len(x)/2)
        plt.scatter(x[start:],y[start:],s=5)
    plt.title('Gibbs simulation')
    plt.xlabel('theta[0]')
    plt.ylabel('theta[1]')
    plt.savefig('./gibbs_sampling_scatter.png', format='png', dpi=600)
    plt.close()

