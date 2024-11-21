# Игра камень-ножницы-бумага
#
# Необходимо написать игру "камень ножницы бумага". Как работает игра. Мы запускаем файл.
# Далее программа спрашивает нас, что мы выбираем (игрок) – камень/ножницы/бумага.
# Далее боту рандомится камень/ножницы/бумага. Затем происходит проверка кто выиграл
#
# Решить задачу необходимо используя 4 функции:
#
# 1) получение выбора игрока
# 2) получение выбора бота
# 3) расчет победителя
# 4) функция play в которой идет игра
#
# Дополнительно:
# 1) добавьте возможность сыграть не один раз, а несколько
# 2) после завершения игры сделайте вывод кол-ва побед и поражений (предусмотрите вариант ничьи)

import random

def players_move():
    global players
    players = input('Для игры введите: \n1 - камень, \n2 - ножницы или \n3 - бумага, \nдля выхода из игры введите 0 \n>>> ')
    try:
        if int(players) >= 0 and int(players) < 4:
            players = int(players)
        else:
            print()
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            print('!!! Введено неправильное значение !!!')
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            print()
            players_move()
    except  Exception:
        print()
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        print('!!! Введено неправильное значение !!!')
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        print()
        players_move()


def bot_move():
    global lst, bot
    lst = ['камень', 'ножницы', 'бумага']
    bot = random.choice(lst)
    return bot

def win():
    global player_win, bot_win, draw, win_
    if lst[players - 1] == bot:
        win_ = 'Ничья'
        draw  = draw  + 1
    elif ((players == 1 and bot == ('ножницы'))
          or (players == 2 and bot == ('бумага'))
          or (players == 3 and bot == ('камень'))):
        win_ = ('Победил игрок')
        player_win = player_win + 1
    else:
        win_ = 'Победа компьютера'
        bot_win = bot_win + 1

    return win_, player_win, bot_win, draw

def play ():
    global win_
    global total_win, player_win, bot_win, draw
    players_move()
    bot_move()
    while players > 0 and players <= 3:
            win()
            total_win = player_win + bot_win + draw
            print()
            print('-----------------------------------------------------------------------------------------------')
            print(win_)
            print('-----------------------------------------------------------------------------------------------')
            print()
            players_move()
            bot_move()
    return total_win

player_win = 0
bot_win = 0
draw = 0
total_win = 0
win_ = ''

play()

print()
print('==============================================================================================')
print(f'     Всего сыграно {total_win} игр, ничьих {draw}, побед игрока {player_win}, побед компьютера {bot_win}')
print('==============================================================================================')