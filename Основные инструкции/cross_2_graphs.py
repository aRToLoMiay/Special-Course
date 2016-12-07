# -*- coding: utf-8 -*-
# Упражнение 9. Точка пересечения двух кривых

def f(x):
	return x

def g(x):
	return x**2

from math import fabs
N = input("Введите число N: ")
varepsilon = input("Введите число varepsilon: ")
h = 8 / N
for i in range(N):
	x = i*h - 4
	if fabs(f(x) - g(x)) < varepsilon:
		print "В точке %.3f значения функций совпадают." % (x)
	else:
		print "В точке %.3f значения функций не совпадают." % (x)
		
