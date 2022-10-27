# Найти наибольший общий делитель числа (НОД):


## Способ 1:

num1 = int(input('Please enter first natural number: '))
num2 = int(input('Please enter second natural number: '))

gcd = 1

if num1 > num2:
    num1, num2 = num2, num1

for i in range(1, num1 + 1):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i
           
print(f'GCD of {num1} and {num2} = {gcd}')

## Способ 2:

import math

print(f'GCD of {num1} and {num2} = {math.gcd(num1, num2)}')

## Способ 3:

def gcd_rec(x, y): 
    if (y == 0):
        return x
    else: 
        return gcd_rec(y, x % y) 

print(f'GCD of {num1} and {num2} = {gcd_rec(num1, num2)}')

## Способ 4:

a = int(input('Please enter first natural number: '))
b = int(input('Please enter second natural number: '))

if a < b:
    a, b = b, a

while b!=0:
    a, b = b, a % b

print(a)

## Способ 5:

while a != b:
    if a > b:
        a -= b
    else:
        b -= a

print(a)