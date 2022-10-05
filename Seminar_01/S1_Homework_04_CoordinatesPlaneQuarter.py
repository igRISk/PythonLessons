# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных 
# координат точек в этой четверти (x и y).

quarter = int(input('Enter number of quarter(from 1 to 4): '))
while quarter < 1 or quarter > 4:
    quarter = int(input('Please enter valid number of quarter - FROM 1 TO 4: '))

match quarter:
    case 1:
        print('Coordinates of quarter 1: x > 0, y > 0')
    case 2:
        print('Coordinates of quarter 2: x < 0, y > 0')
    case 3:
        print('Coordinates of quarter 3: x < 0, y < 0')
    case _:
        print('Coordinates of quarter 4: x > 0, y < 0')