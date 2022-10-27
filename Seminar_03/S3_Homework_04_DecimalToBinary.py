# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def DecimalToBinary(dec_num):
    l = 0
    tmp = dec_num
    while tmp != 0:
        tmp = tmp // 2
        l += 1
    lst = []
    for i in range(l - 1, -1, -1):
        lst.append(dec_num % 2)
        dec_num = dec_num // 2
    bin_num = reversed(lst)
    return bin_num

num = int(input('Enter decimal number please: '))
print(*DecimalToBinary(num), sep = '')


## Вариант 2:

a = int(input('Введите число для перевода = '))
b = ''
while a != 0:
    b = str(a % 2) + b
    a = a // 2
print(b)


## Вариант 3:

a= int(input('Введите число = '))
print(bin(a))