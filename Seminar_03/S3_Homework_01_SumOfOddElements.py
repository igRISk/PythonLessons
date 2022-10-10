# Задайте список из нескольких чисел. Напишите программу, которая найдёт 
# сумму элементов списка, стоящих на нечётной позиции.
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

lst = list(map(int, input('Enter some numbers separated by spaces: ').split()))
sum = 0

for i in range(1, len(lst), 2):
    sum = sum + lst[i]

print('Sum of odd elements:', sum)