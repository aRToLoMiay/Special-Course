# -*- coding: utf-8 -*-
# Упражнение 9. Форматированный вывод на экран

from math import pi

x = pi
y = 2
z = pi * y

print u"Умножение %.5f на %.0f даёт %.3f" % (x, y, z)