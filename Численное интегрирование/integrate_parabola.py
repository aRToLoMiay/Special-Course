# -*- coding: utf-8 -*-
# Упражнение 3.3: Вычислить просто интеграл

from trapezoidal import trapezoidal as trap
from rectangular import rectangular as rect
from math import fabs

f = lambda x: x*(x-1)
a = 2
b = 6
n1 = 2
n2 = 100
exact = 208. / 3 - 16
print "При использовании формулы трапеций:"
print "Для n = 2, |I - exact| = %f" % (fabs(trap(f, a, b, n1) - exact))
print "Для n = 100, |I - exact| = %f" % (fabs(trap(f, a, b, n2) - exact))
print "При использовании формулы прямоугольников:"
print "Для n = 2, |I - exact| = %f" % (fabs(rect(f, a, b, n1) - exact))
print "Для n = 100, |I - exact| = %f" % (fabs(rect(f, a, b, n2) - exact))