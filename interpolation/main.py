# -*- coding: utf-8 -*-

import numpy as np
import matplotlib  
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import runge
import trace
import piecewise_linear_interpolation as pli
import piecewise_hermite3_interpolation as phi
import spline3

def main():
	#给定样本点及其函数值，以及导数值，以及边界点处的二阶导数值
	#根据这些样本点来进行插值
	x = list(np.linspace(-5,5,111))
	y = [runge.runge(i) for i in x]
	dy = [runge.derivative(i) for i in x]
	boundary = [runge.derivative_2(i) for i in [y[0],y[-1]]]
	
	#给定一批新的样本点，计算其真实函数值
	#这批新的样本点是用来考察各种插值方法的预测精度的
	new_x = list(np.linspace(-5,5,200))
	true_y = np.array([runge.runge(i) for i in new_x])
	#绘制真实函数值图像
	plt.plot(new_x, true_y, 'k', label='true')
	
	#绘制分段线性插值的预测图
	new_y = pli.piecewise_linear_interpolation(x, y, new_x, sort=True)
	plt.plot(new_x, new_y, 'b', label='pli')
	print('Error of pli:')
	#记录分段线性插值的预测误差
	error_pli = true_y - new_y
	#print(error_pli)
	print(sum([abs(i) for i in error_pli]))
	
	#绘制分段三次Hermite插值的预测图
	new_y = phi.piecewise_hermite3_interpolation(x, y, dy, new_x, sort=False)
	plt.plot(new_x, new_y, 'y', label='phi')
	print('Error of phi:')
	#记录分段三次Hermite插值的误差
	error_phi = true_y - new_y
	#print(error_phi)
	print(sum([abs(i) for i in error_phi]))
	
	#绘制样条插值的预测图
	new_y = spline3.spline3(x, y, new_x, boundary, sort=False)
	plt.plot(new_x, new_y, 'r', label='spline')
	print('Error of spline:')
	#记录样条插值的预测误差
	error_spline = true_y - new_y
	#print(error_spline)
	print(sum([abs(i) for i in error_spline]))
	
	#对比三种插值方法的预测情况
	plt.title('Comparision among Three Interpolation Methods')
	plt.xlabel('x')  
	plt.ylabel('y')  
	#plt.legend(bbox_to_anchor=[0.3, 1]) 
	plt.legend(loc='best')
	plt.savefig('./interpolation.png', format='png', dpi=900)
	plt.close()

	#绘制三种插值方法的误差图
	plt.plot(new_x, error_pli, 'b', label='pli')
	plt.plot(new_x, error_phi, 'y', label='phi')
	plt.plot(new_x, error_spline, 'r', label='spline')
	plt.title('Errors of Three Interpolation Methods')
	plt.xlabel('x')  
	plt.ylabel('error')  
	#plt.legend(bbox_to_anchor=[0.3, 1]) 
	plt.legend(loc='best')
	plt.savefig('./error.png', format='png', dpi=900)
	plt.close()

if __name__ == '__main__':
	main()
