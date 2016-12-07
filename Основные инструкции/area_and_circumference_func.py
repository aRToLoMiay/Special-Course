# -*- coding: utf-8 -*-
# Упражнение 3. Функции для вычисления площади круга и длины окружности

from math import pi

AreaCircle = lambda x: pi*r**2
LengthCircle = lambda x: 2*pi*r

r = input("Введите радиус окружности: ")
C = LengthCircle(r)
A = AreaCircle(r)

print "При радиусе = %.3f длина окружности = %.3f, площадь круга = %.3f" % (r, C, A)