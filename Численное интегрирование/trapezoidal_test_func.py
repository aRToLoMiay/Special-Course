# -*- coding: utf-8 -*-
# Упражнение 3.1: Вычисления вручную для формулы трапеций

from trapezoidal import trapezoidal as trap
from math import fabs

def testTrapezoidal(trap):
	a = 1.
	b = 3.
	n = 4
	exact = 41.
	eps = 10e-15
	f = lambda x: 2*x**3
	if (fabs(trap(f, a, b, n) - exact) < eps):
		return True
	else:
		return False


result = testTrapezoidal(trap)
if result:
	print "Полученный результат верен."
else:
	print "Полученный результат ошибочен."