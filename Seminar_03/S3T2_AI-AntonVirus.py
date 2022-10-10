# Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников.
# Теперь он использует их в качестве серверов "Пегого дудочника". 
# Помогите владельцу фирмы отыскать все зараженные холодильники.
# Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр, 
# и если в ней присутствует слово "anton" (необязательно рядом стоящие буквы, главное 
# наличие последовательности букв), то холодильник заражен и нужно вывести номер холодильника, 
# нумерация начинается с единицы

# В первой строке подаётся число n – количество холодильников. 
# В последующих n строках вводятся строки, содержащие латинские строчные буквы и цифры, 
# в каждой строке от 5 до 100 символов.

# Программа должна вывести номера зараженных холодильников через пробел. 
# Если таких холодильников нет, ничего выводить не нужно.

## Пример 1: 
## 6
## 222anton456
## a1n1t1o1n1
## 0000a0000n00t00000o000000n
## gylfole
## richard
## ant0n
## Зараженные холодильники: 1 2 3

## Пример 2:
## 9
## osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen
## anton
## aoooooooooontooooo
## elelelelelelelelelel
## ntoneeee
## tonee
## 253235235a5323352n25235352t253523523235oo235523523523n
## antoooooooooooooooooooooooooooooooooooooooooooooooooooon
## unton
## Зараженные холодильники: 1 2 7 8

import re

path = 'D:\GeekBrainsLessons\PythonProjects\Seminar_03\WorkFiles\S3T2_example1.txt'
data = open(path, 'r')

total_num_fridges = int(data.readline(1))
fridges_data = [line.strip() for line in data]

data.close()

infection_sign = ''.join(f'.*?{i}' for i in 'anton')
infection_list = []

for i in range(1, total_num_fridges+1):
    if re.search(infection_sign, fridges_data[i]):
        infection_list.append(i)

print(infection_list)