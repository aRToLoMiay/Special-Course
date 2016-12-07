# -*- coding: utf-8 -*-
# Упражнение 3.1: Вычисления вручную для формулы трапеций

from rectangular import rectangular as rect
from math import fabs

def testRectangular(rect):
	a = 1.
	b = 3.
	n = 4
	exact = 39.5
	eps = 10e-15
	f = lambda x: 2*x**3
	if (fabs(rect(f, a, b, n) - exact) < eps):
		return True
	else:
		return False


result = testRectangular(rect)
if result:
	print "Полученный результат верен."
else:
	print "Полученный результат ошибочен."