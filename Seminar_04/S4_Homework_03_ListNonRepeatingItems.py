# Задайте последовательность чисел. Напишите программу, которая выведет 
# список неповторяющихся элементов исходной последовательности.


## Вариант 1

numbers = list(map(int, input('Enter some numbers separated by spaces: ').split()))
uniqlist = []
count = 0

for i in numbers:
    for j in range(0, len(numbers)):
        if i == numbers[j]:
            count += 1
    if count < 2:
        uniqlist.append(i)
    count = 0

print(uniqlist)


## Вариант 2

b = [1, 1, 2, 2, 3, 455, 66, 66, 2, 1]
a = []
for i in b:
    if b.count(i) == 1:
        a.append(i)

print(a)


## Вариант 3

import random

list1 = [random.randint(-10, 10) for i in range(random.randrange(3, 10))]
print(list1)

list2 = [i for i in list1 if list1.count(i) == 1]
print(list2)