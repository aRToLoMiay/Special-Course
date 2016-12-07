# -*- coding: utf-8 -*-
# Упражнение 16. Проверка прямой линии

from random import uniform

f = lambda x: 4*x + 1
left = 0
right = 10
a = -4
c = 2
flag = 0
eps = 10e-6
for i in range(100):
	x = uniform(left, right)
	if (float)((f(x) - f(c))) / (x - c) - a < eps:
		print "Для х = %f выполняется. Итерация i = %d" % (x, i+1)
		flag += 1
if flag == 0:
	print "Условие ни разу не было выполнено."