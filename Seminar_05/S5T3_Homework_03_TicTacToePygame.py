import pygame
import sys
 
def check_control(mas, sign):  # ПРОВЕРКА ВЫЙГРАША
    zero = 0
    capriz_1 = -50
    capriz_2 = -50
    for row in mas:  # _1_ПРОВЕРКА
        capriz_1 += 115
        zero += row.count(0)
        if row.count(sign) == 3:  # ЕСЛИ КОЛ-ВО ЗНАКОВ В СТРОКЕ - ТРИ, ТО ВОЗВРАТ ТОГО САМОГО ЗНАКА
            if sign == 'x':
                pygame.draw.line(screen, green, (30, capriz_1), (330, capriz_1), 10)
            else:
                pygame.draw.line(screen, red, (30, capriz_1), (330, capriz_1), 10)
            return sign
    for col in range(3):  # _2_ПРОВЕРКА
        capriz_2 += 115
        if mas[0][col] == sign and mas[1][col] == sign and mas[2][col] == sign:  # ЕСЛИ КОЛ-ВО ЗНАКОВ В КОЛОНКЕ - ТРИ, ТО ВОЗВРАТ ТОГО САМОГО ЗНАКА
            if sign == 'x':
                pygame.draw.line(screen, green, (capriz_2, 30), (capriz_2, 330), 10)
            else:
                pygame.draw.line(screen, red, (capriz_2, 30), (capriz_2, 330), 10)
            return sign
    if mas[0][0] == sign and mas[1][1] == sign and mas[2][2] == sign:  # ЕСЛИ ЗНАК НА ДИАГОНАЛЕ # _3_ПРОВЕРКА
        if sign == 'x':
            pygame.draw.line(screen, green, (30, 30), (330, 330), 20)
        else:
            pygame.draw.line(screen, red, (30, 30), (330, 330), 20)
        return sign
    if mas[0][2] == sign and mas[1][1] == sign and mas[2][0] == sign:  # ЕСЛИ ЗНАК НА ДИАГОНАЛЕ # _4_ПРОВЕРКА
        if sign == 'x':
            pygame.draw.line(screen, green, (330, 30), (30, 330), 20)
        else:
            pygame.draw.line(screen, red, (330, 30), (30, 330), 20)
        return sign
    if zero == 0:
        return "НИЧЬЯ"  # ЕСЛИ НЕТ НИ ОДНОЙ ПУСТОЙ КЛЕТКИ (ОПРЕДЕЛЯЕТ ЭТО "ZERO")
    return False  # ЕСЛИ УСЛОВИЕ НЕ ВЫПОЛНИЛОСЬ, ТО False
 
 
pygame.init()
size_block = 100  # ШИРИНА
margin = 15  # ОТСТУП
width = height = size_block * 3 + margin * 4  # ШИРИНА И ДЛИНА ЭКРАНА
 
size_window = (width, height)  # СОЗДАНИЕ ЭКРАНА
screen = pygame.display.set_mode(size_window)
pygame.display.set_caption("крестики-нолики")
 
black = (0, 0, 0)  # ЦВЕТА В ФОРМАТЕ RGB
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
mas = [[0] * 3 for i in range(3)]  # МАСИВ С НУЛЯМИ, ОНИ ОЗНАЧАЮТ ЧТО КЛЕТКА СВОБОДНА
query = 0  # 1 2 3 4 5 6 7 8 9
game_over = False  # ИЗНАЧАЛЬНО ОНА False
while True:
    for event in pygame.event.get():  # ЦИКЛ ОБРАБОТКИ СОБЫТИЙ
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:  # ЕСЛИ ТИП СОБЫТИЯ - НАЖАТЕЕ КНОПКИ МЫШИ И НЕ game_over
            x_mouse, y_mouse = pygame.mouse.get_pos()  # X,Y КООРДИНАТЫ МЫШИ
            col = x_mouse // (size_block + margin)  # УЗНАЁМ КОЛОНКУ ПУТЁМ ДЕЛЕНИЯ МЫШИ(КООРДИНАТА) НА ШИРИНА БЛОКА + ОТСТУП
            row = y_mouse // (size_block + margin)  # УЗНАЁМ СТРОКУ ПУТЁМ ДЕЛЕНИЯ МЫШИ(КООРДИНАТА) НА ШИРИНА БЛОКА + ОТСТУП
            if mas[row][col] == 0:  # ДОСТУП ТОЛЬКО ЕСЛИ ТАМ 0
                if query % 2 == 0:  # ЕСЛИ ОСТАТОК ТО XO"
                    mas[row][col] = "x"  # ТО "X"
                else:
                    # РОБОТ
                    mas[row][col] = "o"  # ЕСЛИ НЕ, ТО "O"
                query += 1  # УВЕЛИЧИВАЕМ ПЕРЕМЕННУЮ НА ОДИН
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:  # ЕСЛИ ТИП СОБЫТИЯ ЭТО НАЖАТЕЕ НА ПРОБЕЛ
            game_over = False  # ДЕЛАЕМ ИГРУ ОПЯТЬ ПРАВДОЙ
            mas = [[0] * 3 for i in range(3)]  # ДЕЛАЕМ ОПЯТЬ ПУСТОЙ МАСИВ
            query = 0  # ОБНУЛЯЕМ СЧЁТЧИК (ОПЯТЬ ХОДИТ ПЕРВЫЙ ИГРОК)
            screen.fill(black)
            
    if not game_over:  # ЕСЛИ ИГРА НЕ ЗАКОНЧЕНА
        for row in range(3):  # ЦИКЛ ОБХОДИТ КОЛ-ВО СТОРК И СТОЛБЦОВ
            for col in range(3):
                if mas[row][col] == "x":  # ЕСЛИ ТАМ 'Х' ТО КРАСНЫЙ
                    color = red
                elif mas[row][col] == "o":  # ЕСЛИ ТАМ 'О' ТО ЗЕЛЁНЫЙ
                    color = green
                else:
                    color = white
                x = col * size_block + (col + 1) * margin  # КООРДИНАТЫ "X"
                y = row * size_block + (row + 1) * margin  # КООРДИНАТЫ "Y"
                pygame.draw.rect(screen, color, (x, y, size_block, size_block))  # ПОЯВЛЯЮТСЯ КВАДРАТИКИ
                if color == red:  # ЕСЛИ С КРЕСТИКОМ
                    pygame.draw.line(screen, white, (x + 5, y + 5), (x + size_block - 5, y + size_block - 5), 5)  # РИСУЕМ ЛИНИЮ ИЗ  (x + 5, y + 5),  В (x + size_block - 5, y + size_block - 5) С ТОЛЩИНОЙ В 5 ПИКСЕЛЕЙ
                    pygame.draw.line(screen, white, (x + size_block - 5, y + 5), (x + 5, y + size_block - 5), 5)  # РИСУЕМ ЛИНИЮ ИЗ    (x + size_block - 5, y + 5)     В (x + 5, y + size_block - 5) С ТОЛЩИНОЙ В 5 ПИКСЕЛЕЙ
                elif color == green:  # ЕСЛИ С НОЛИКОМ
                    pygame.draw.circle(screen, white, (x + size_block // 2, y + size_block // 2), size_block // 2 - 3, 5)  # КООРДИНАТЫ ЦЕНТРА ДЕЛЁНЫЕ НА ДВА, РАДИУС ПОЛОВИНА БЛОКА МИНУС ТРИ ТОЛЩИНА В ПЯТЬ ПИКСЕЛЕЙ
    if (query - 1) % 2 == 0:  # ЕСЛИ ИГРОК ЧЁТНЫЙ
        game_over = check_control(mas, 'x')
    else:  # ЕСЛИ ИГРОК НЕ ЧЁТНЫЙ
        game_over = check_control(mas, 'o')  # СОХРАНЯЕТСЯ ЭТО В ПЕРЕМЕННОЙ  game_over
 
 
    pygame.display.update()  # ИЗМЕНЕНИЯ