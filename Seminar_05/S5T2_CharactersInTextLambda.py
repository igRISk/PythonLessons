# Объявите анонимную (лямбда) функцию для определения вхождения в переданную ей строку фрагмента "plr". То есть, функция должна возвращать True, если такой фрагмент присутствует в строке и False - в противном случае.

txt = input('Please input some text: ')
fragment = 'plr'

res = lambda text, chars: chars in text
print(res(txt, fragment))

## Вариант 2:

f = lambda x: x.count('plr') > 0
print(f(txt))

## Вариант 3:

print((lambda x: 'plr' in x)(input('Please input some text: ')))

# contains = lambda s, sample='plr': sample in s
# s = input()
# print(contains(s))