# Напишите программу, которая на вход принимает 5 значений и находит максимальное из них:

print()
array_numbers = list(map(int, input('Enter 5 numbers separated by space: ').split()))
print(max(array_numbers))
print()