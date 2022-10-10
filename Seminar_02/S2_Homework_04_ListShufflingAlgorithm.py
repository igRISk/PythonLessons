# 1) Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#    Найдите произведение элементов на указанных позициях.
# 2) Реализуйте алгоритм перемешивания списка.

import random

n = int(input('Enter a natural number: '))
numbers = list(range(-n,n+1))
print(numbers)

## Вариант 1 - готовый алгоритм в Python:
random.shuffle(numbers)
print(numbers)

## Вариант 2 - алгоритм, написанный когда-то на Pascal или на C, уже не помню:
for i in range(len(numbers)-1, 0, -1):
    r = random.randint(0, i-1)
    tmp = numbers[i]
    numbers[i] = numbers[r]
    numbers[r] = tmp
print(numbers)