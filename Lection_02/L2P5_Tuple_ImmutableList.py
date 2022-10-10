# Кортежи (tuple): это неизменяемый список

t = ()
print(type(t))          # tuple
t = (1,)
print(type(t))          # tuple
t = (28, 9, 1990)
print(type(t))          # tuple

colors = ['red', 'green', 'blue']
print(colors)           # ['red', 'green', 'blue']
t = tuple(colors)
print(t)                # ('red', 'green', 'blue')

# Примеры:

a = (3, 1, 41, 2)
print(a)
print(a[-2])

for item in t:
    print(item)

tup = tuple(['red', 'green', 'blue'])
red, green, blue = tup
print('r:{} g:{} b:{}'.format(red, green, blue))
