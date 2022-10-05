# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# Для N = 5: 1, -3, 9, -27, 81

n = int(input('Enter N, please: '))
x = -3

for i in range(0, n):
    print(x**i, end = " ")

#    if i == 1: 
#        result = 1
#        print(result , end = ", ")
#    elif i == n:
#        result = result * -3
#        print(result , end = " ")
#    else: 
#        result = result * -3
#        print(result , end = ", ")