# -*- coding: utf-8 -*-
# Упражнение 10. Сортировка массива чисел

import sys
import codecs
sys.stdout = codecs.getwriter('cp866')(sys.stdout,'replace')

from random import *

ar = []
for i in range(6):
	ar.append(uniform(0, 10))
print ar
for i in range(i-1, 0, -1):
	for j in range(i):
		if ar[j] > ar[j+1]:
			ar[j+1], ar[j] = ar[j], ar[j+1]
print ar
	