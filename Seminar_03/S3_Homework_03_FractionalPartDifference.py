# Задайте список из вещественных чисел. Напишите программу, которая найдёт 
# разницу между максимальным и минимальным значением дробной части элементов.
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

lst = list(map(float, input('Enter some numbers separated by spaces: ').split()))
max = 0
min = lst[0]

for i in range(0, len(lst)):
    fractional_part = round(lst[i] - int(lst[i]), 2)
    if max < fractional_part:
        max = fractional_part
    if min > fractional_part:
        min = fractional_part

print(round(max-min, 2))