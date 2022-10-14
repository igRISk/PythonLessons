# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# - 6782 -> 23
# - 0,56 -> 11


## Вариант 1:

num = input('Enter a number: ')
numlst = list(num)
sum = 0

if '.' in numlst:
    numlst.remove('.')

for i in range(len(numlst)):
    sum = sum + int(numlst[i])

print(num, sum, sep = ' -> ')


## Вариант 2:

numb = float(input('Enter a number: '))
summ = 0
for el in str(numb):
    if el !='.':
        summ += int(el)
print(summ)


## Вариант 3:

in_number = float(input('Enter a number: '))
num_int = int(str(in_number).replace('.', ''))
sum = 0
while num_int > 0:
    cut_digit = num_int % 10
    sum = sum + cut_digit
    num_int //= 10
print(f"{in_number}", f"{sum}", sep=" -> ")

