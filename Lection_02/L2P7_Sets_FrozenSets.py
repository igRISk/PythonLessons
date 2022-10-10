# Set - множество, это "контейнер", содержащий не повторяющиеся элементы в случайном порядке:

colors = {'red', 'green', 'blue'}
print(type(colors))                 # set

colors.add('red')
print(colors)                       # {'red', 'green', 'blue'}

colors.add('gray')
print(colors)                       # {'red', 'green', 'blue', 'gray'}

colors.remove('red')
print(colors)                       # {'green', 'blue', 'gray'}

colors.discard('red')               # также удаляет, но если элемента нет, то без ошибки
print(colors)                       # {'green', 'blue', 'gray'}

colors.clear()                      # очистить множество, { }
print(colors)

# Действия с множествами:

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy()                        # c = {1, 2, 3, 5, 8}
u = a.union(b)                      # u = {1, 2, 3, 5, 8, 13, 21}
i = a.intersection(b)               # i = {8, 2, 5} 
dl = a.difference(b)                # dl = {1, 3}
dr = b.difference(a)                # dr = {13, 21}

q = a \
    .union(b) \
    .difference(a.intersection(b))  # {1, 21 , 3, 13}

## Неизменяемые множества: 

s = frozenset(a)