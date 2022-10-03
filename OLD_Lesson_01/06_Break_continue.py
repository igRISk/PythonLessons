# break - выход из цикла, выполнилось условие или нет
# continue - переход на следующую итерацию цикла
#            (команды в цикле после continue не выполняются)

# пример break:
name = None
while True:
    name = input('Кто создатель Python? ')
    if name == 'Гвидо':
        break
    print('Неправильно, попробуйте еще раз)')
print ('Верно!')

# пример continue:
number = 0
end_number = int(input('Введите до какого числа: '))
while number <= end_number:
    if number % 2 != 0:
        number += 1
        continue
    print(number)
    number += 1