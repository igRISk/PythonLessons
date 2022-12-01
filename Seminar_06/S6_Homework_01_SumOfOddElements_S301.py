# Задача: предложить улучшения кода для уже решённых задач:
#    С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension


## Задайте список из нескольких чисел. Напишите программу, которая найдёт 
## сумму элементов списка, стоящих на нечётной позиции.
## - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


###  Исходное решение без улучшения:

lst = list(map(int, input('Enter some numbers separated by spaces: ').split()))
sumnum = 0

for i in range(1, len(lst), 2):
    sumnum = sumnum + lst[i]

print('Sum of odd elements:', sumnum)

###  Решение с улучшением (enumerate + list comprehension):

lst = list(map(int, input('Enter some numbers separated by spaces: ').split()))
print('Sum of odd elements:', sum([j for i, j in enumerate(lst) if i % 2]))