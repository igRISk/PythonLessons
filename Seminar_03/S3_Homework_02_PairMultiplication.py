# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# - [2, 3, 4, 5, 6] => [12, 15, 16]
# - [2, 3, 5, 6] => [12, 15]

lst = list(map(int, input('Enter some natural numbers separated by spaces: ').split()))
reslst = []
i = 0
j = int(len(lst)) - 1
lenreslst = len(lst) // 2 + len(lst) % 2

while lenreslst > i:
    reslst.append(lst[i] * lst[j])
    i += 1
    j -= 1

print('List of multiplicated pairs:', reslst)