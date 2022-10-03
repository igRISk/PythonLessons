# пример цикла while

name = input('Кто создатель Python? ')

while name != 'Гвидо':
    print('Неправильно, попробуйте еще раз)')
    name = input('Кто создатель Python? ')

print ('Верно!')

# вывод четных чисел от 0 до n

number = 0
end_number = int(input('Введите до какого числа: '))

while number <= end_number:
    if number % 2 == 0:
        print(number)
    number += 1
