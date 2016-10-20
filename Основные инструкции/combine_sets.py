# -*- coding: utf-8 -*-
# Упражнение 12. Вычисление комбинаций

import sys
import codecs
sys.stdout = codecs.getwriter('cp866')(sys.stdout,'replace')

print u"Для id состоящего из двух букв и трёх цифр может быть 26*26*10*10*10 = 676000 комбинаций"

def sum(list):
	S = 0
	for i in range(len(list)):
		S += list[i]
	return S

def getCombinations(list):
	result = []
	listInd = []
	for i in range(len(list)):
		listInd.append(len(list[i])-1);
	j = len(list)-1
	i = 0
	while sum(listInd) != 0:
		print listInd
		result.append([])
		for k in range(len(list)):
			result[i].append(list[k][listInd[k]])
		i += 1
		while (listInd[j] == 0):
			j -= 1
		if (j >= 0) and (j != len(list) - 1) and (listInd[j] == 0):
			for k in range(j, len(list)-1, 1):
				listInd[k] = len(list[k]) - 1
			j = len(list) - 1
		else:
			listInd[j] -= 1
	return result

matrix = []
a1 = [1, 2, 3, 4]
a2 = [10, 100]
matrix.append(a1)
matrix.append(a2)
print getCombinations(matrix)
			
		