# Задана натуральная степень k. Сформировать случайным образом список 
# коэффициентов (значения от 0 до 100) многочлена и записать в файл 
# многочлен степени k:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

indexes = {"0": "\u2070",
           "1": "\u00B9",
           "2": "\u00B2",
           "3": "\u00B3",
           "4": "\u2074",
           "5": "\u2075",
           "6": "\u2076",
           "7": "\u2077",
           "8": "\u2078",
           "9": "\u2079",
           "-": "\u207B"}

def degree(a: int):
    degrees = ""
    tmp = str(a)
    for char in tmp:
        degrees += indexes[char] or ""
    return degrees

k = int(input('Enter a natural number (polynomial degree): '))
limit_coefficient = 100
formula = ''

for i in range(k, -1, -1):
    c = random.randint(0, limit_coefficient)
    if len(formula) > 2 and c > 0 and i!=0:
        formula += ' + '
    if c > 0 and k > 0:
        if i == 1:
            formula += str(c) + '*x'
        elif i == k:
            formula += str(c) + '*x' + degree(i)   
        elif i == 0:
            formula += ' + ' + str(c)
        else:
            formula += str(c) + '*x' + degree(i)

if 'x' in formula:
    formula += ' = 0'
else:
    formula = 'Sorry, that formula does not exist!'
print(formula)

path = 'D:\GeekBrainsLessons\PythonProjects\Seminar_04\S4WorkFiles\S4HW4_out.txt'
data = open(path, 'wb')

data.write(formula.encode('UTF-8'))
data.close()