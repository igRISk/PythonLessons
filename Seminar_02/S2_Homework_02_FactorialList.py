# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


## Вариант 1:
n = int(input('Enter a natural number: '))
num = 1
num_list = []

for i in range(0, n):
    num = num * (i+1)
    num_list.append(num)
print(num_list)

## Вариант 2:
import math
print([math.factorial(n) for n in range(1,n+1)])