# Дана строка текста. Напишите программу для подсчета стоимости строки, исходя из того, 
# что один любой символ (в том числе пробел) стоит 60 копеек. 
# Ответ дайте в рублях и копейках в соответствии с примерами.
# #1 - Привет, как дела?!
# #1 - 10 р. 80 коп.
# #2 - Тимур - лучший математик на свете!!
# #2 - 21 р. 0 коп.

str_user = input('Please enter text: ')

# Вариант 1:
cost = len(str_user) * 60
print(f'{cost // 100} р. {cost % 100} коп.')

# Вариант 2:
rub=(len(str_user)*60)//100
kop=(len(str_user)*60)-rub*100
print(rub,"р.",kop,"коп.")