# List - списки, расширенные свойства и особенности:

## Пример 1:

list1 = [1, 2, 3]
list2 = list1                   # list2 будет только ссылкой на list1, а не скопируется

for e in list1:
    print(e, end = ' ')
for e in list2:
    print(e, end = ' ')

print()
list1[0] = 123                  # меняем значение 0 в list1
list2[1] = 333                  # меняем значение 1 в list2
for e in list1:
    print(e, end = ' ')         # результат одинаковый [123, 333, 3]
for e in list2:
    print(e, end = ' ')         # результат одинаковый [123, 333, 3]

## Пример 2:

print()
list3 = [1,2,3,4,5]             # создаем list [1,2,3,4,5]

list3.pop()                     # удаление последней позиции
print(list3)                    # [1, 2, 3, 4]

print(list3.pop())              # 4 - удаление последней позиции и вывод количества оставшихся
print(list3)                    # [1, 2, 3]

list3.pop(1)                    # удаление позиции с индексом 1
print(list3)                    # [1, 3]

list3.insert(1, 11)             # добавляем число 11 в позицию с индексом 1
print(list3)                    # [1, 11, 3]

list3.append(333)             # добавляем число 333 в конец
print(list3)                    # [1, 11, 3, 333]