# else (после while) - мы выполняем дествия после того,
# как вышли из цикла while, когда условия цикла стало неверным

number = 0

while number <=100:
    print(number)
    number += 1
    if number == 33:
        break
else:
    print('else - end')

print('real end')