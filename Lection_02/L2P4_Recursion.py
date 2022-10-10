def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)

e = 10
list = []
for i in range(1, e + 1):
    list.append(fib(i))
print(list)