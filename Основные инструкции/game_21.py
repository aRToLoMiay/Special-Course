# -*- coding: utf-8 -*-
# Упражнение 14. Игра 21

import sys
import codecs
sys.stdout = codecs.getwriter('cp866')(sys.stdout,'replace')

from random import randint

S = 0
S += randint(0, 10)
f = 0
print u"Ваше стартовое значение = %d" % (S)
f = raw_input(u"Введите Y для генерации ещё одного числа или любой другой символ для прекращения игры: ")
while f == 'Y':
	if S > 21:
		f = 'N'
	else:
		S += randint(0, 10)
		print u"Ваше текущее значение - %d" % (S)
		f = raw_input(u"Введите Y для генерации ещё одного числа или любой другой символ для прекращения игры: ")


if S > 21:
	print u"Вы проиграли! Ваш результат = %d" % (S)
elif S == 21:
	print u"Поздравляем! Вы победили и набрали 21 очко!"
else:
	print u"Ваш результат = %d" % (S)