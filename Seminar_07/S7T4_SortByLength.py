# 3)На вход программы поступает список наименований рек, записанных в одну строчку через пробел. 
# Необходимо отсортировать этот список в порядке убывания длин названий. 
# Результат вывести в одну строчку через пробел.
# Лена Енисей Волга Дон -> Енисей Волга Лена Дон


## Вариант 1:

txt = ('Енисей Волга Лена Дон').split()
print(sorted(txt, key=len, reverse=True))

## Вариант 2:

txt.sort(key= lambda x: len(x), reverse=True)
print(txt)

## Вариант 3:

s=sorted(input().split(), key=lambda x: len(x))[::-1]
print(*s)