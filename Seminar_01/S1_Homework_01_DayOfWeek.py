# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
# является ли этот день выходным.
# - 6 -> да
# - 7 -> да
# - 1 -> нет

day = int(input('Please enter the number of the day of the week: '))

while day < 1 or day > 7:
    day = int(input('Week have only 7 days, please enter valid number: '))

if day == 6 or day == 7:
    print(f'{day} -> yes')
else:
    print(f'{day} -> no')