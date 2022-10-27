# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты 
# у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint

def bot_player(candy_left):
    if candy_left <= 28:
        bptake = candy_left
    elif candy_left > 29 and candy_left < 56:
        bptake = candy_left - 29
    else:
        bptake = 28
    print ('Player 2 (bot) takes', bptake, 'candies')
    return bptake


candies = 100 #2021
game_mode = input('Please select a game mode:\n 1 - player vs player \n 2 - player vs computer\n')
turn = randint(1, 2)
print ('\n> Player number', turn, 'is the first to move <\n')

while candies > 0:
    if turn == 1:
        p1take = int(input('Player 1, please enter number of candies: '))
        while p1take < 1 or p1take > 28 or p1take > candies:
            print("Player 1, enter correct amount, we have", candies, "candies and you can't take less than 1 or more than 28: ", end = '')
            p1take = int(input())
        candies -= p1take
        if candies > 0:
            turn = 2
    else:
        if game_mode == 1: 
            p2take = int(input('Player 2, please enter number of candies: '))
            while p2take < 1 or p2take > 28 or p2take > candies:
                print("Player 2, enter correct amount, we have", candies, "candies and you can't take less than 1 or more than 28: ", end = '')
                p2take = int(input())
            candies -= p2take
            if candies > 0:
                turn = 1
        else:
            candies -= bot_player(candies)
            if candies > 0:
                turn = 1
    print('\n> Dear players, now we have', candies, 'candies on the table <\n')

print('   --->>> And the winner is player', turn, '<<<---   \n')