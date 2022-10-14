def func(x):
    return x**2

g = func
print(func(2))
print(g(2))

print(type(func))
print(type(g))

##################################################

def calc1(x):
    return x+10

def calc2(x):
    return x*10

def math(op, x):
    print(op(x))

math(calc1, 10)
math(calc2, 10)

##################################################

# def sum(x, y):
#     return x+y

sum = lambda x, y: x+y

f = sum

def mult(x, y):
    return x*y

def calc(op, a, b):
    print(op(a, b))
    return op(a, b)

calc(sum, 4, 5)
calc(f, 4, 5)
calc(lambda x, y: x+y, 4, 5)

