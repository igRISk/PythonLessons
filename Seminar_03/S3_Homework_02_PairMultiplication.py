# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# - [2, 3, 4, 5, 6] => [12, 15, 16]
# - [2, 3, 5, 6] => [12, 15]


## Вариант 1:

lst = list(map(int, input('Enter some natural numbers separated by spaces: ').split()))
reslst = []
i = 0
j = int(len(lst)) - 1
lenreslst = len(lst) // 2 + len(lst) % 2

while lenreslst > i:
    reslst.append(lst[i] * lst[j])
    i += 1
    j -= 1

print('List of multiplicated pairs:', reslst)


## Вариант 2:

import math

nums = list(map(int, input("Задайте список из нескольких чисел через пробел: ").split()))
mult = []

for i in range(math.ceil(len(nums)/2)):
    mult.append(nums[i] * nums[-i-1])

print(f'{nums} => {mult}')


## Вариант 3:

import random
b = int(input('Введите кол-во чисел в списке for 2# = '))
list_b = list(random.randint(0, 10) for i in range(b))
print(list_b)
proiz_b = list(list_b[i]*list_b[-1*(1+i)] for i in range(b//2+1*(b%2)))
print(proiz_b)