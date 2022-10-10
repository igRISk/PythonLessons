# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

num = int(input('Enter decimal number please: '))
lst1 = [0, 1]
lst2 = []

for i in range(2, num + 1):
    lst1.append(lst1[i-1] + lst1[i-2])

lst2 = lst1.copy()

for i in range(2, num + 1):
    if i % 2 == 0:
        lst2[i] *= -1

lst2.pop(0)
lst2.reverse()
lst3 = lst2 + lst1

print(lst3)