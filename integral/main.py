# -*- coding: utf-8 -*-

import numpy as np
import compound_trapezoid as ct
import compound_simpson as cs
import gauss as gs
import romberg as rb
import math

def main():
	start = 0
	end = math.pi/2
	num = 8
	integral = ct.compound_trapezoid(start, end ,num)
	print('9点复化梯形公式计算结果：')
	print(integral)
	num = 8
	integral = cs.compound_simpson(start, end, num)
	print('9点复化辛普森公式计算结果：')
	print(integral)
	num = 3
	integral = gs.gauss(start, end ,num)
	print('3点高斯公式计算结果是：')
	print(integral)
	num = 4
	integral = gs.gauss(start, end ,num)
	print('4点高斯公式计算结果是：')
	print(integral)
	integral = rb.romberg(start, end, k=4)
	print('龙贝格方法计算结果是：')
	print(integral)
	#integral = rb.romberg(start, end, ep=1e-6, choose_k=False)
	#print(integral)

if __name__ == '__main__':
	main()
