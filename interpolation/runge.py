# -*- coding: utf-8 -*-

def runge(x):
	return 1/(1+x*x)

def derivative(x):
	return -2*x/((1+x*x)**2)

def derivative_2(x):
	return (8*x**2*(1+x**2) - 2*(1+x**2)**2)/((1+x**2)**4)

if __name__ == '__main__':
	pass
