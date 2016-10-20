# -*- coding: utf-8 -*-
# Упражнение 3. Функции для вычисления площади круга и длины окружности

import sys
import codecs
sys.stdout = codecs.getwriter('cp866')(sys.stdout,'replace')

from math import pi

AreaCircle = lambda x: pi*r**2
LengthCircle = lambda x: 2*pi*r

r = input(u"Введите радиус окружности: ")
C = LengthCircle(r)
A = AreaCircle(r)

print u"При радиусе = %.3f длина окружности = %.3f, площадь круга = %.3f" % (r, C, A)