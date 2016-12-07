# -*- coding: utf-8 -*-
# Упражнение 15. Линейная интерполяция

def linInterpolation(y, t):
	i = 0
	while i <= t:
		i += 1
	if i == len(y):
		result = y[i-1]
	else:
		result = (t - i + 1)*(y[i] - y[i-1]) + y[i-1]
	return result

def userMenu(y):
	print "Введите время в отрезке [0, %d] для расчёта приближённого значения функции." % (len(y)-1)
	t = input("И любое другое для прерывания работы программы: ")
	while t >= 0 and t <= len(y)-1:
		print "Для введённого t = %f, приближённое значение функции = %f" % (t, linInterpolation(y, t))
		t = input("Повторите ввод значения t: ")

y = [4.4, 2.0, 11.0, 21.5, 7.5]
t = 2.5
print "Для значения = %.3f, получим приближённое значение функции = %f" % (t, linInterpolation(y, t))
t = 3.1
print "Для значения = %.3f, получим приближённое значение функции = %f" % (t, linInterpolation(y, t))
userMenu(y)