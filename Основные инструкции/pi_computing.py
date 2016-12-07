# -*- coding: utf-8 -*-
# Упражнение 11. Вычисление числа пи

def Leybniz(N):
	S = 0.0
	for i in range(N+1):
		S += 1. / ((4*i + 1)*(4*i + 3))
	S *= 8
	return S

def Eyler(N):
	S = 0.0
	for i in range(N):
		S += 1. / (i+1)**2
	S *= 6
	S = S**(0.5)
	return S

from math import pi
import matplotlib.pyplot as plt

print 4**(0.5)
N = input("Введите число слагаемых: ")
x = range(1, N+1)
y = []
for i in range(N):
	y.append(Leybniz(x[i]))
	y[i] -= pi
plt.plot(x, y)
y = []
for i in range(N):
	y.append(Eyler(x[i]))
	y[i] -= pi
plt.plot(x, y)
plt.show()
