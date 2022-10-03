# Напишите программу, которая принимает на вход два числа, и проверяет, 
# является ли одно квадратом другого
# - 5,25->да
# - 25,5->да
# - 8,9->нет

print()

a = int(input('Enter a number, please: '))
b = int(input('Enter one more number, please: '))

if a == b**2 or b == a**2:
    print(f'{a},{b} -> yes')
else:
    print(f'{a},{b} -> no')
    
print()