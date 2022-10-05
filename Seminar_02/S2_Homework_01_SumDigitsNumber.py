# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# - 6782 -> 23
# - 0,56 -> 11

num = input('Enter a number: ')
numlst = list(num)
sum = 0

if '.' in numlst:
    numlst.remove('.')

for i in range(len(numlst)):
    sum = sum + int(numlst[i])

print(num, sum, sep = ' -> ')
