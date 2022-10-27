# Создайте программу для игры в ""Крестики-нолики"".

play_field = [['-','-','-'], 
              ['-','-','-'], 
              ['-','-','-']]

freecells = 9
nobody_won = True
pmarker = 'X'

def chkwin(array):
    if (array[0][0] == array[1][0] == array[2][0] != '-') or \
       (array[0][1] == array[1][1] == array[2][1] != '-') or \
       (array[0][2] == array[1][2] == array[2][2] != '-') or \
       (array[0][0] == array[0][1] == array[0][2] != '-') or \
       (array[1][0] == array[1][1] == array[1][2] != '-') or \
       (array[2][0] == array[2][1] == array[2][2] != '-') or \
       (array[0][0] == array[1][1] == array[2][2] != '-') or \
       (array[2][0] == array[1][1] == array[0][2] != '-'):
        return True
    else:
        return False

def printfield(array):
    print()
    for i in range(0, 3):
        print(array[0][i], array[1][i], array[2][i])
    print()

while nobody_won and freecells > 0:
    pmove = list(map(int, input('Enter the cell number in the array separated by a space: ').split()))
    while pmove[0] < 0 or pmove[0] > 2 or pmove[1] < 0 or pmove[1] > 2 or play_field[pmove[0]][pmove[1]] != '-': 
        pmove = list(map(int, input('Wrong move, try again: ').split()))
    play_field[pmove[0]][pmove[1]] = pmarker
    printfield(play_field)
    nobody_won = not(chkwin(play_field))
    freecells -= 1
    if nobody_won and pmarker == 'X':
        pmarker = '0'
    elif nobody_won and pmarker == '0': 
        pmarker = 'X'

if nobody_won:
    print('This is the end! \nAnd nobody won =)\n')
else:
    print('This is the end! \nAnd won the game:', pmarker,'\n')    