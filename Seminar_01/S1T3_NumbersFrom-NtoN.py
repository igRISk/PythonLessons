# Напишите программу, которая будет на вход принимать число N 
# и выводить числа от -N до N

print()
n = int(input('Enter a number: '))
for i in range(-n, n+1):
    print(i, end=' ')
print()