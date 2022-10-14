# Задайте натуральное число N. Напишите программу, которая составит 
# список простых множителей числа N.

number = int(input('Enter a natural number: '))

simple_mult_list = []
m = 2

while m*m <= number:
    if number % m == 0:
        simple_mult_list.append(m)
        number //= m
    else:
        m += 1
if number > 1:
    simple_mult_list.append(number)

print(simple_mult_list)