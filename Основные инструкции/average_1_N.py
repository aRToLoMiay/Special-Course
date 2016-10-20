# -*- coding: utf-8 -*-
# Упражнение 6.  Среднее значение целых чисел

import sys
import codecs
sys.stdout = codecs.getwriter('cp866')(sys.stdout,'replace')

def AverageValue(N):
	return 0.5 * (1 + N)

N = input(u"Введите целое число: ")
print u"Среднее значение целых чисел = %.3f" % (AverageValue(N))