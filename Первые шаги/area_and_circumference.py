# -*- coding: utf-8 -*-
# Упражнение 3. Площадь круга и длина окружности

from math import pi
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

r = 2
A = pi*r**2
C = 2*pi*r

print "Площадь круга = %f \nДлина окружности = %f" % (A, C)