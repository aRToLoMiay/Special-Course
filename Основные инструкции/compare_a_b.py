# -*- coding: utf-8 -*-
# Упражнение 2. Сравнение целых чисел a и b

import sys
import codecs
sys.stdout = codecs.getwriter('cp866')(sys.stdout,'replace')

a = input(u"Введите целое число a:")
b = input(u"Введите целое число b:")

if a < b:
	print u"a - наименьшее из введённых чисел"
elif a == b:
	print u"a и b равны"
else:
	print u"b - наименьшее из введённых чисел"