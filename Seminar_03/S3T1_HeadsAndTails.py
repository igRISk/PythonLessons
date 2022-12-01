# Орел и решка: дана строка текста, состоящая из букв русского алфавита "О" и "Р". 
# Буква "О" – соответствует выпадению Орла, а буква "Р" – соответствует выпадению Решки. 
# Напишите программу, которая подсчитывает наибольшее количество подряд выпавших Решек.
# Программа должна вывести наибольшее количество подряд выпавших Решек.
# - ОРРОРОРООРРРО -> 3
# - ООООООРРРОРОРРРРРРР -> 7
# - ООООРРРРОРОРРРРРРРРООРОРОРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРР -> 31

op_text = input('Enter a certain amount of capital Russian letters "О" and "Р" without spaces: ')
op_letters = list(op_text)

qty_p = 0
maxq_p = 0

# Вариант 1:

for char in op_letters:
    if char == 'Р':
        qty_p += 1
    else:
        qty_p = 0
    if maxq_p < qty_p:
        maxq_p = qty_p

print(op_text, maxq_p, sep = ' -> ')

# Вариант 2:

for i in op_letters:
    if i == 'Р' and maxq_p <= qty_p:
        qty_p += 1
        maxq_p = qty_p
    elif i == 'Р' and maxq_p > qty_p:
        qty_p += 1
    else:
        qty_p = 0

print(op_text, maxq_p, sep = ' -> ')

# Вариант 3:

s = op_text
t = 0

while "Р"*(t+1) in s:
    t+=1
if t!=0:
    print(t)
else:
    print(0)