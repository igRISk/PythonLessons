# Задача: предложить улучшения кода для уже решённых задач:
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

## Напишите программу, которая будет на вход принимать число N 
## и выводить числа от -N до N


### Вариант 1, исходный:

print()
n = int(input('Enter a number: '))
for i in range(-n, n+1):
    print(i, end=' ')
print()


### Решение с улучшением (list comprehension):

n = int(input('Enter a number: '))
print(*[x for x in range(-n,n)])