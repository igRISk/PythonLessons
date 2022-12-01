# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


## Вариант 1:

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


## Вариант 2:

def neg_fibonacci(numb):
    array = [1, 0, 1]
    for i in range(1, numb):
        array.insert(0, array[1] - array[0])
        array.append(array[-2] + array[-1])
    return array

n = int(input('Enter decimal number please: '))
print(neg_fibonacci(n))