# Напишите программу, в которой пользователь вводит целое число,
# а программа определяет сколько в этом числе цифр 0, 1, 2 ... 9
# def main_():
#     try:
#         num = int(input('Введите целое число: '))
#         str_ = str(num)
#         list_ = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#         k = 0
#
#         for i in list_:
#             a = str_.count(str(i))
#             print(f'Цифр {i} в числе {num} встречается {a} раз')
#     except Exception:
#         print('Вы ввели не целое число')
#         main_()
#
# main_()


# Напишите программу, в которой пользователь вводит целое число,
# а программа каждую цифру в этом силе меняет на дополнение до 9

def main_():
    try:
        num = int(input('Введите целое число: '))
        str_ = str(num)
        s = ''
        for i in str_:
            a = 9 - int(i)
            s += str(a)

        print(int(s))

    except ValueError:
        print('Вы ввели не целое число')
        main_()

main_()

