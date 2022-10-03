# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат.

xyz = list(map(int, input('Enter integer numbers X, Y, Z separated by space: ').split()))

while len(xyz) != 3:
    xyz = list(map(int, input('You should enter 3 numbers X, Y, Z separated by space: ').split()))

def checkPredicate(x):
    left = not (x[0] or x[1] or x[2])
    right = not x[0] and not x[1] and not x[2]
    result = left == right
    return result

if checkPredicate(xyz) == True:
    print('The statement ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z is true!')
else:
    print('The statement ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z is false!')