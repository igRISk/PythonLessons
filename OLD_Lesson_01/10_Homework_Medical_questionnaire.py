name = input('Please, enter your name: ')
surname = input('Please, enter your surname: ')
age = int(input('Please, enter your age: '))
weight = int(input('Please, enter your weight: '))

if age % 10 == 1:
    particle = 'год'
elif age % 10 == 2 or age % 10 == 3 or age % 10 == 4:
    particle = 'года'
else:
    particle = 'лет'

if age < 30 and (weight >= 50 and weight < 120):
    print(name, surname, age, particle, 'вес', weight, '- you are in great shape =)')
elif age > 30 and age <= 40 and (weight < 50 or weight > 120):
    print(name, surname, age, particle, 'вес', weight, ' - you should take care of yourself')
elif age > 40 and (weight < 50 or weight > 120):
    print(name, surname, age, particle, 'вес', weight, '- you need a doctor!')
else:
    print (name, surname, age, particle, 'вес', weight, '- you are so good, man!')

