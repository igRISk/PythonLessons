# Задайте список из вещественных чисел. Напишите программу, которая найдёт 
# разницу между максимальным и минимальным значением дробной части элементов.
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


## Вариант 1:

lst = list(map(float, input('Enter some numbers separated by spaces: ').split()))
minfp = lst[0]
maxfp = 0

for i in range(0, len(lst)):
    fractional_part = round(lst[i] - int(lst[i]),3)
    print(fractional_part)
    if maxfp < fractional_part:
        maxfp = fractional_part
    if minfp > fractional_part:
        minfp = fractional_part

print(round(maxfp-minfp, 2))


## Вариант 2:

list = list(map(float, input('Enter some numbers separated by spaces: ').split()))
mix_list = []

for i in list:
    mix_list.append(round(i-int(i), 2))

print(list, end=' => ')
print(max(mix_list) - min(mix_list))