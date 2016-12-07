# -*- coding: utf-8 -*-
# Упражнение 12. Вычисление комбинаций

print "Для id состоящего из двух букв и трёх цифр может быть 26*26*10*10*10 = 676000 комбинаций"

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
		result.append([])
		for k in range(len(list)):
			result[i].append(list[k][listInd[k]])
		i += 1
		while (listInd[j] == 0):
			j -= 1

		if (j >= 0):
			listInd[j] -= 1
			for k in range(j+1, len(list), 1):
				listInd[k] = len(list[k]) - 1
			j = len(list) - 1
	
	result.append([])
	for k in range(len(list)):
		result[i].append(list[k][listInd[k]])
	return result

def getNumberCombinations(list):
	result = 1
	for i in range(len(list)):
		result *= len(list[i])
	return result

rank = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
lear = ['C', 'D', 'H', 'S']
digit = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
letter = ['A', 'B', 'E', 'I', 'K', 'M', 'H', 'O', 'P', 'C', 'T', 'X']
matrix = [rank, lear]
deck = getCombinations(matrix)
print "Количество карт = %d. Сама колода:" % (len(deck))
print deck
matrix = [digit, digit, digit, digit, letter, letter]
regNumber = getNumberCombinations(matrix)
print "Количество всех номеров = %d." % (regNumber)