# Пример 1, импорт из другого файлика:

import L1P8_OLD_Functions as f
x = 1
print(f.func(x))

# Пример 2, использование аргументов:

def new_string(symbol, count = 3):
    return symbol * count

print(new_string('!', 5))   # !!!!!
print(new_string('!'))      # !!!
print(new_string(4))        # 12

# Пример 3, неограниченное количество аргументов:

def concatenatio(*params):
    res: str = ""
    for item in params:
        res += item
    return res

print(concatenatio('a', 's', 's', 'w'))     # asdw
print(concatenatio('a', '1', 's', '2'))     # a1d2

def concatenatioInt(*params):
    res = 0
    for item in params:
        res += item
    return res

print(concatenatioInt(1, 2, 3, 4))     # 10 (сумма всех элементов)