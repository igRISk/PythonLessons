# Арифметические операции
# +, -, * , / , %, //, **
# Логические операции
# >, >= , <, <=, == , !=
# not, and, or
# is, is not, in, not in

a = 22
b = 8
c = a // b
print(c)
c = a % b
print(c)

a = 1.3123
b = 3
c = round(a * b, 2)
print(c)

a = 3
a += 5
print(a)

a = 1 < 4 and 5 > 2
print(a)

a = 1 == 2
print(a)

a = 'qwe'
b = 'qwe'
print(a == b)

a = 1 < 3 < 5
print(a)

func = 1
T = 4
x = 2

print(func<T>(x))

f = [1,2,3,4]
print(2 in f)

is_odd = f[0] % 2 == 0
print(is_odd)
is_odd = not f[0] % 2
print(is_odd)