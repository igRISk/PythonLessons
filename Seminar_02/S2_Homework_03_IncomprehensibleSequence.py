# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}


## Вариант 1, если я правильно понял формулу:
n = int(input('Enter a natural number: '))
dic = {n: round((1+1/n)**n, 2) for n in range(1, n+1)}
print (dic)

## Вариант 2, если следовать примеру:
n = int(input('Enter a natural number: '))
print ({n: 4+3*(n-1) for n in range(1, n+1)})