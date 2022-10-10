# Задайте список. Напишите программу, которая определит, присутствует ли в заданном 
# списке строк некое число.

lst = input('Enter some numbers separated by spaces: ').split()
num = input('Enter a number to find in the list: ')

if num in lst:
    print(lst, num, 'Yes', sep = " -> ")
else:
    print(lst, num, 'No', sep = " -> ")