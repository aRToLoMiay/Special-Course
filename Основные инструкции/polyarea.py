# -*- coding: utf-8 -*-
# Упражнение 5. Площадь многоугольника

import sys
import codecs
sys.stdout = codecs.getwriter('cp866')(sys.stdout,'replace')

def SquareTriangle(x1, y1, x2, y2, x3, y3):
	return 0.5*((x1 - x3)*(y2 - y3) - (x2 - x3)*(y1 - y3))
	

x = []
y = []
n = input(u"Введите число точек: ")
for i in range(n):
	x.append(input())
	y.append(input())

S = 0
for i in range(n - 2):
	S += SquareTriangle(x[i], y[i], x[i+1], y[i+1], x[i+2], y[i+2])

print u"Площадь многоугольника = %f" % (S)