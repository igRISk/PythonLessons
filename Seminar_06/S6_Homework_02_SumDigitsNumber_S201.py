# Задача: предложить улучшения кода для уже решённых задач:
#    С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension


## Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
## - 6782 -> 23
## - 0,56 -> 11


### Вариант 1, исходный:

num = input('Enter a number: ')
numlst = list(num)
sumn = 0

if '.' in numlst:
    numlst.remove('.')

for i in range(len(numlst)):
    sumn = sumn + int(numlst[i])

print(num, sumn, sep = ' -> ')

### Решение с улучшением (list comprehension):

num2 = input('Enter a number: ').split()
print(*num2, sum([int(x) for x in num if x !='.']), sep = ' -> ')