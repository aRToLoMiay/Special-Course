# -*- coding: utf-8 -*-
# Программа для вычисления положения мяча при вертикальном движении
# с использованием функции
# Упражнение 1. Ошибки с двоеточиями, отступами и т.п.

def y(t):
   v0 = 5       # Начальная скорость
   g = 9.81     # Ускорение свободного падения
   return v0*t - 0.5*g*t**2
	
t = 0.6      # Время
print y(t)
t = 0.9
print y(t)

# при "def y(t)" - SyntaxError: invalid syntax
# без отступа перед "v0 = 5" - IndentationError: expected an indented block
# "v0 = 5" с тремя пробелами - IndentationError: unexpected indent
# "yt)" - SyntaxError
# "y()" - TypeError
# "print y()" - TypeError: y() takes exactly 1 argument (0 given)