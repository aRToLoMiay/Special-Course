# -*- coding: utf-8 -*-
# Упражнение 8. Площадь прямоугольника в сравнении с кругом

import sys
import codecs
sys.stdout = codecs.getwriter('cp866')(sys.stdout,'replace')

from math import pi

r = 10.6
sc = pi*r**2
a = 1.3
b = 0
while a*b < sc:
	b += 1
b -= 1
print u"Наименьшее целое b = %.3f" % (b) 