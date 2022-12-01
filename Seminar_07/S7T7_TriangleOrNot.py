# 5. Напишите функцию triangle(a, b, c), которая принимает на вход 
# три длины отрезков и определяет, можно ли из этих отрезков составить треугольник.
# triangle(1, 1, 2) - 
# triangle(7, 6, 10) - 


## Вариант 1:

t = list(map(int, input('Enter 3 numbers (sides of a triangle): ').split()))
if t[0]+t[1]>t[2] and t[1]+t[2]>t[0] and t[0]+t[2]>t[1]:
    print(t, '-> это трегуольник')
else:
    print(t, '-> это НЕ трегуольник')

## Вариант 2:

triangle = lambda a,b,c: print(f'({a}, {b}, {c}) -> это треугольник') if a+b>c and a+c>b and b+c>a else print(f'({a}, {b}, {c}) -> это НЕ треугольник')
triangle (1, 1, 2) 
triangle (7, 6, 10)