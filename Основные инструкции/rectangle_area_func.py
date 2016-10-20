# -*- coding: utf-8 -*-
# Упражнение 4. Функция для вычисления площади прямоугольника

import sys
import codecs
sys.stdout = codecs.getwriter('cp866')(sys.stdout,'replace')

AreaRectangle = lambda x, y: x*y

b = input(u"Введите стороны прямоугольника: ")
c = input()

A = AreaRectangle(b, c)

print(u"Площадь прямоугольника со сторонами: %.3f и %.3f будет равна %.3f ") % (b, c, A)