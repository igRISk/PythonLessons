# 1.Вводится список целых чисел в одну строчку через пробел. 
# Необходимо оставить в нем только двузначные числа. Реализовать программу с 
# использованием функции filter. 
# Результат отобразить на экране в виде последовательности оставшихся чисел в 
# одну строчку через пробел.


## Вариант 1:

nums = input('Please input some numbers: ').split()
filtered_nums = ' '.join(filter(lambda x: len(x)==2, nums))
print(filtered_nums)


## Вариант 2:

print(*filter(lambda x: len(str(abs(int(x)))) == 2, input('Please input some numbers: ').split()))


## Вариант 3:

arr = list(map(int, input("Введите последовательность чисел через пробел: ").split()))
print(list(filter(lambda e: 9 < e < 100, arr)))