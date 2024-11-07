# Игра крестики - нолики


def draw_area():
    for i in area:
        print(*i)

def chek_winner():
    if area[0][0] == area[0][1] == area[0][2] == 'X':
        return 'X'
    if area[1][0] == area[1][1] == area[1][2] == 'X':
        return 'X'
    if area[2][0] == area[2][1] == area[2][2] == 'X':
        return 'X'
    if area[0][0] == area[1][1] == area[2][2] == 'X':
        return 'X'
    if area[2][0] == area[1][1] == area[0][2] == 'X':
        return 'X'
    if area[0][0] == area[1][0] == area[2][0] == 'X':
        return 'X'
    if area[0][1] == area[1][1] == area[2][1] == 'X':
        return 'X'
    if area[0][2] == area[1][2] == area[2][2] == 'X':
        return 'X'

    if area[0][0] == area[0][1] == area[0][2] == '0':
        return '0'
    if area[1][0] == area[1][1] == area[1][2] == '0':
        return '0'
    if area[2][0] == area[2][1] == area[2][2] == '0':
        return '0'
    if area[0][0] == area[1][1] == area[2][2] == '0':
        return '0'
    if area[2][0] == area[1][1] == area[0][2] == '0':
        return '0'
    if area[0][0] == area[1][0] == area[2][0] == '0':
        return '0'
    if area[0][1] == area[1][1] == area[2][1] == '0':
        return '0'
    if area[0][2] == area[1][2] == area[2][2] == '0':
        return '0'

area = [['*','*','*'],['*','*','*'],['*','*','*']]
print('Добро пожаловать в игру')
print('-----------------------')
for turn in range(1, 10):
    print(f'Ход: {turn}')
    if turn % 2 ==0:
        turn_char = '0'
        print('Ходят нолики')
    else:
        turn_char = 'X'
        print('Ходят крестики')
    row = int(input('Введите номер строки (1, 2, 3): ')) - 1
    columns = int(input('Введите номер столбца (1, 2, 3): ')) - 1
    if area[row][columns] == '*':
        area[row][columns] = turn_char
    else:
        print('Ячейка занята!!! Вы пропускаете ход !!!')
        draw_area()
        continue

    draw_area()

    if chek_winner() == 'X':
        print('!!! Победа крестиков !!!')
        break
    if chek_winner() =='0':
        print('!!! Победа ноликов !!!')
        break
    if chek_winner() == '*' or turn == 9:
        print('Ничья')

