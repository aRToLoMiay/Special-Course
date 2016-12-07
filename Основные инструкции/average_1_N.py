# -*- coding: utf-8 -*-
# Упражнение 6.  Среднее значение целых чисел

import platform
if platform.system() == "Windows":
	import sys
	import codecs
	sys.stdout = codecs.getwriter('cp1251')(sys.stdout,'replace')

def AverageValue(N):
	return 0.5 * (1 + N)

N = input("Введите целое число: ")
print u"Среднее значение целых чисел = %.3f" % (AverageValue(N))