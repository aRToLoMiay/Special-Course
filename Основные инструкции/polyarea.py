# -*- coding: utf-8 -*-
# Упражнение 5. Площадь многоугольника

x = []
y = []
n = input("Введите число точек: ")
print "Введите координаты точек:"
for i in range(n):
	x.append(input())
	y.append(input())
x.append(x[0])
y.append(y[0])
S = 0
for i in range(n):
	S += (x[i] + x[i+1]) * (y[i+1] - y[i])
S *= 0.5
print S
#print "Площадь многоугольника = %f" % (S)