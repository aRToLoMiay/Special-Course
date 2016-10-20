# -*- coding: utf-8 -*-
# Упражнение 13. Частота случайных чисел

import sys
import codecs
sys.stdout = codecs.getwriter('cp866')(sys.stdout,'replace')

from random import randint
N = input(u"Введите число N: ")
ar = []
M = 0
for i in range(N):
	ar.append(randint(1,6))
	if ar[i] == 6:
		M += 1

print u"Сгенерированный список: "
print ar
print u"Отношение M/N = %.5f" % (float(M)/N)