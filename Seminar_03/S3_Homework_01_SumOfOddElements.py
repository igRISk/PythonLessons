# Задайте список из нескольких чисел. Напишите программу, которая найдёт 
# сумму элементов списка, стоящих на нечётной позиции.
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


## Вариант 1:

import numbers

lst = list(map(int, input('Enter some numbers separated by spaces: ').split()))
sumnum = 0

for i in range(1, len(lst), 2):
    sumnum = sumnum + lst[i]

print('Sum of odd elements:', sumnum)


## Вариант 2:

nums = list(map(int, input('Enter some numbers separated by spaces: ').split()))
print('Sum of odd elements:', sum(nums[1::2]))