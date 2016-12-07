# -*- coding: utf-8 -*-
# Упражнение 13. Частота случайных чисел

from random import randint
N = input("Введите число N: ")
ar = []
M = 0
for i in range(N):
	ar.append(randint(1,6))
	if ar[i] == 6:
		M += 1

print "Сгенерированный список: "
print ar
print "Отношение M/N = %.5f" % (float(M)/N)