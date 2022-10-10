lst = [1, 2, 3, 'hello', 4.5, 'world', True]
print(lst)
lst2 = lst[:] # записать в переменную lst2 все значения, lst2 = lst создаст только ссылку на lst

ran = range(1, 6)
numbers = list(ran)
print(numbers)

print(f'Number of elements = {len(numbers)}')

for i in numbers:
    i *= 2
    print(i)
print(numbers)

colors = ['red', 'green', 'blue']

for e in colors:
    print(e*2)

colors.append('gray') # добавить в конец
print(colors)

colors.remove('red') # удалить элемент 'red'
print(colors)
del colors[0] # удалить элемент 0
print(colors)