# -*- coding: utf-8 -*-
# Упражнение 8. Площадь прямоугольника в сравнении с кругом

from math import pi

r = 10.6
sc = pi*r**2
a = 1.3
b = 0
while a*b < sc:
	b += 1
b -= 1
print "Наименьшее целое b = %.3f" % (b) 