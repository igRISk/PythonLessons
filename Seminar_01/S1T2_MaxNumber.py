# Напишите программу, которая на вход принимает 5 значений и находит максимальное из них:

array_numbers = []
num_of_elements = 5
maxvalue = 0

for i in range(0,num_of_elements):
    number = int(input('Enter a number, please: '))
    array_numbers.append(number)
    if i == 0:
        maxvalue = array_numbers[i]
    if array_numbers[i] > maxvalue:
        maxvalue = array_numbers[i]

print (f'{array_numbers} -> {maxvalue}')