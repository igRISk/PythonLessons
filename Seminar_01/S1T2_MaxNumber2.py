# Напишите программу, которая на вход принимает 5 значений и находит максимальное из них:

print()
array_numbers = list(map(int, input('Enter 5 numbers separated by space: ').split()))
maxvalue = array_numbers[0]
for i in range(len(array_numbers)):
    if array_numbers[i] > maxvalue:
        maxvalue = array_numbers[i]

print (f'{array_numbers} -> {maxvalue}')
print()