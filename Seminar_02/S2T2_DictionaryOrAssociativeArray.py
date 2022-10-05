# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

## вариант 1:
n = int(input('Enter N, please: '))
dic = {n: 3*n+1 for n in range(1, n+1)}
print (dic)

## вариант 2:
x = 1
for i in range(1, n+1):
    x = 3 * i + 1
    if i == 1:
        print(f'[{i}: {x},', end = ' ')
    elif i == n:
        print(f'{i}: {x}]')
    else:
        print(f'{i}: {x},', end = ' ')
