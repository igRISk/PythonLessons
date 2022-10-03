name = 'Кеша'
age = 2

print('Привет, меня зовут', name, 'мне', age, 'года')
print('Привет, меня зовут', name, 'мне', age, 'года', sep='/')

print(name)
print(age)

print('----------------------------------------------')
print(name, end=';')
print(age, end=' ')
print('end', end='')
print()

name = input('Как тебя зовут: ')
print('Привет, ', name, '!', sep='')

age = int(input('Сколько тебе лет: '))
period = 20
age_period = age + period
print('Через', period, 'лет тебе будет', age_period)