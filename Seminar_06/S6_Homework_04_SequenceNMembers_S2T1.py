# Задача: предложить улучшения кода для уже решённых задач:
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

## Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
## Для N = 5: 1, -3, 9, -27, 81


### Вариант 1, исходный:

n = int(input('Enter N, please: '))
x = -3

for i in range(0, n):
    print(x**i, end = " ")
print()


### Решение с улучшением (list comprehension):

n = int(input('Enter N, please: '))
print (*[(-3)**n for n in range(0, n)])