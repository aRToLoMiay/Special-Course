# -*- coding: utf-8 -*-
# Упражнение 4. Объём трёх кубов

from numpy import linspace

L = linspace(1, 3, 3)
V = L**3
for i in range(3):
	print "Длина сторону = %3.3f Объём куба = %3.3f" % (L[i], V[i])