# Вычислить число Пи c заданной точностью d:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
# Pi = 3,141592653589793238462643 (для проверки алгоритма)


# Вариант 1 (ряд Лейбница):

accuracy = float(input('Enter a number in the given interval $10^{-1} ≤ d ≤10^{-10}$: '))

n = float(1)
s1 = 4/(2*n-1)
n += 1
s2 = s1-4/(2*n-1)


while (s1-s2) > accuracy:
    n += 1
    s1=s2+4/(2*n-1)
    n += 1
    s2=s1-4/(2*n-1)

acc = 0
while accuracy < 1:
    accuracy *= 10
    acc += 1

Pi = (s1+s2)/2
Pi = float(int(Pi*(10**acc)) / 10**acc)

print(Pi)