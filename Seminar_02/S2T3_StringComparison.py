# Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.

from itertools import count

a = input('Please enter text for line 1: ')
b = input('Please enter text for line 2: ')

## Вариант 1:
if len(a) > len(b):
    print(a.count(b))
else:
    print(b.count(a))

## Вариант 2 (неправильное решение, так как сравнение побуквенное):
qty = 0

if len(b) > len (a):
    a, b = b, a

for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            qty += 1

print(qty)