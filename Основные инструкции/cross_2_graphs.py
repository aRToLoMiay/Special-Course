# -*- coding: utf-8 -*-
# Упражнение 9. Точка пересечения двух кривых

import sys
import codecs
sys.stdout = codecs.getwriter('cp866')(sys.stdout,'replace')

def f(x):
	return x

def g(x):
	return x**2

from math import fabs
N = input(u"Введите число N: ")
varepsilon = input(u"Введите число varepsilon: ")
h = 8 / N
for i in range(N):
	x = i*h - 4
	if fabs(f(x) - g(x)) < varepsilon:
		print u"В точке %.3f значения функций совпадают." % (x)
	else:
		print u"В точке %.3f значения функций не совпадают." % (x)
		
