# Types are dinamical

value = None
print(type(value))

a = 123
b = 1.23
print(type(a))
print(type(b))
value = 12334
print(type(value))

s = 'Hello " " world!'
t = "Hello ' ' world!"
u = "Hello \" \nworld!" # \n - перенос строки 
print(s)
print(t)
print(u)

print('{} - {} - {}'.format(a, b, s))
print('{1} - {2} - {0}'.format(a, b, s))
print(f'{a} - {b} - {s}')
