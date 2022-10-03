# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).
# x=34; y=-30 -> 4
# x=2; y=4-> 1
# x=-34; y=-30 -> 3

x = int(input('Enter x coordinate: '))
y = int(input('Enter y coordinate: '))

while x == 0 or y == 0:
    if x == 0:
        x = int(input("Coordinates can't be 0, enter valid coordinate x: "))
    if y == 0:
        y = int(input("Coordinates can't be 0, enter valid coordinate y: "))

if x > 0 and y > 0:
    print(f'x={x}; y={y} -> 1 ')
elif x > 0 and y < 0:
    print(f'x={x}; y={y} -> 4 ')
elif x < 0 and y < 0:
    print(f'x={x}; y={y} -> 3 ')
else:
    print(f'x={x}; y={y} -> 2 ')