# -*- coding: utf-8 -*-
# Упражнение 7.  Цикл while  с ошибками

import sys
import codecs
sys.stdout = codecs.getwriter('cp866')(sys.stdout,'replace')

sum = 0
i = 1
while i < 11:
	sum += 1
	i += 1
print sum