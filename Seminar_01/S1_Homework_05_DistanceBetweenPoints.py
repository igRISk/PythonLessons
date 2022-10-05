# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

import math

xa = int(input("Enter 'X' coordinate for point A: "))
ya = int(input("Enter 'Y' coordinate for point A: "))
xb = int(input("Enter 'X' coordinate for point B: "))
yb = int(input("Enter 'Y' coordinate for point B: "))

distance = math.sqrt((xa-xb)*(xa-xb)+(yb-ya)*(yb-ya))
print(f'Distance between points A and B: {round(distance, 2)}')