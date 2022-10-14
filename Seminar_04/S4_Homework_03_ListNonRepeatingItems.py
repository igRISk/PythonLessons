# Задайте последовательность чисел. Напишите программу, которая выведет 
# список неповторяющихся элементов исходной последовательности.

numbers = list(map(int, input('Enter some numbers separated by spaces: ').split()))
uniqlist = []
count = 0

for i in numbers:
    for j in range(0, len(numbers)):
        if i == numbers[j]:
            count += 1
    if count < 2:
        uniqlist.append(i)
    count = 0

print(uniqlist)