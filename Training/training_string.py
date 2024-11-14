# Задачи по теме "Работа со строками"
'''
Строки в языке питон являются неизменяемыми объектами. Это значит, что в момент запуска скрипта ячейка памяти,
на которую ссылается строка, не меняется.
Из этого следует, что символы этого типа данных не могут меняться или переписываться.

Любые действия над строками не модифицируют их, а создают новый объект
'''

# Задача_1
'''Напишите функцию search_substr(subst, st), которая принимает 2 строки и определяет,
имеется ли подстрока subst в строке st. В случае нахождения подстроки,
возвращается фраза «Есть контакт!», а иначе «Мимо!».
Должно быть найдено совпадение независимо от регистра обеих строк.'''
from numpy.lib.recfunctions import join_by

# def search_substr(subctr, str):
#     if subctr in str:
#         return('Есть контакт!')
#     else:
#         return ('Мимо!')
#
# str = 'которая принимает 2 строки и определяет'
# subctr = 'определяет'
# output_str = search_substr(subctr, str)
# print(output_str)
# subctr = 'много'
# output_str = search_substr(subctr, str)
# print(output_str)

# Задача_2
'''
Требуется определить индексы первого и последнего вхождения буквы в строке. 
Для этого нужно написать функцию first_last(letter, st), включающую 2 параметра: letter – искомый символ, 
st – целевая строка. В случае отсутствия буквы в строке, нужно вернуть кортеж (None, None), 
если же она есть, то кортеж будет состоять из первого и последнего индекса этого символа.
'''
# def first_last(letter, st):
#     if letter in st:
#         first_letter = st.find(letter)
#         last_letter =  st.rfind(letter)
#     else:
#         first_letter = last_letter = None
#     return first_letter, last_letter
#
# letter = input('Введите символ: ')
# st = 'laksdcnladsuclaiusdycfh'
# print(first_last(letter, st))


# Задача_3
'''
На основании предоставленного отрывка текста определить 3 наиболее часто встречаемых символа в ней. 
Пробелы нужно игнорировать (не учитывать при подсчете). 
Для выведения результатов вычислений требуется написать функцию top3(st). 
Итог работы функции представить в виде строки: «символ – количество раз, символ – количество раз…».
'''
# from collections import Counter
#
# def top3(st):
#     counter_top = Counter(st.replace(' ','')) # Удаляем все пробелы в строке
#     counter_top = counter_top.most_common(3) # Находим три наиболее встречающихся символа
#     return ', '.join([f'{letter} - {cnt}' for letter, cnt in counter_top]) # Выводим полученный результат
#
# st = 'jd;slkf;iдавылп ывфлдвфыз ыфлсдфыва вылсдывьыв ksdaf;asdfq[wkvfasd'
# print(top3(st))

# Задача_4
'''
Задача 4*
Николай решил вспомнить старые времена. В свое время было модно писать сообщения с 
чередующимися заглавной и малой буквами. Он захотел изобрести функцию, 
которая будет делать с любой предоставленной строкой аналогичное. 
Ваша задача: повторить труд студента camel(st) с учетом того, что пробелы и знаки препинания 
не должны портить чередование регистра символов (они в этом процессе не учитываются, но возвращаются в итоговой строке).
'''
# def camel(st):
#     new_st = '' # Создаем новую пустую строку
#     letter_counter = 0 # Устанавливаем счетчик = 0 (индекс символов)
#     for index, val in enumerate(st): # Проходим по каждому символу в строке
#         if val.isalpha(): # проверяем, что символ является алфавитным, т.е., не является знаком препинания или пробелом
#             if letter_counter % 2 == 0: # если индекс буквы четный (т.е. порядковый номер символа нечетный)
#                 new_st +=val.upper() # то буква делается заглавной и добавляется в строку
#             else:
#                 new_st += val.lower() # иначе буква делается строчной и добавляется в строку
#             letter_counter += 1
#         else:
#             new_st += val # если символ является знаком препинания или пробелом, он просто добавляется в строку
#
#     return new_st
#
# st = 'jd;slkf;iдавРЛЛОРЛОРРо - лОРЛОРЛОРЛылп ывфлдвфыз ыфлсдфыва вылсдывьыв ksdaf;asdfq[wkvfasd'
# print(camel(st))

# Задача_5
'''
Задача 5*
Дмитрий считает, что когда текст пишут в скобках (как вот тут, например), его читать не нужно. 
Вот и надумал он существенно укоротить время чтения, написав функцию, которая будет удалять все,
что расположено внутри скобок.
Помогите ленивому Диме разработать функцию shortener(st), которая будет удалять все, 
что внутри скобок и сами эти скобки, возвращая очищенный текст (скобки могут быть вложенными).
'''

# def shertener(st):
#     while '(' in st or ')' in st: # Пока в строке встречаются ( или )
#         left = st.rfind('(') # находим последний символ (
#         right = st.find(')', left) # находим первый символ ) стоящий после последнего (
#         st = st.replace(st[left : right +1],'') # удаляем все что между ( и ) включая скобки
#
#     return st
#
# st = 'Этот текст важен, (это нужно удалить) этот текст важен, (это (нужно (удалить))) этот текст важен, (это (нужно удалить)) этот текст важен'
#
# print(shertener(st))


# Задача_6
'''
Александр решил как-то отобразить в тексте BACKSPACE (т.е. удаление последнего символа). 
Он подумал, что символ @ отлично для этого подходит. 
Всем своим знакомым он дал строки такого вида (например, гр@оо@лк@оц@ва), 
чтобы посмотреть, кому удастся написать функцию cleaned_str(st), возвращающую строку в ее чистом виде.
'''

def cleaned_str(st):
    clean_str = [] # Создадим пустой список для вывода результата
    for symbol in st: # Проходим по всем символам строки st
        if symbol == '@': # Если символ равен @
            clean_str.pop() # вырезаем последний символ в списке вывода
        elif symbol != '@': # Если не равен
            clean_str.append(symbol) # Добавляем символ в список вывода
    return ''.join(clean_str) # Преобразуем полученный список в строку

#print(cleaned_str('гр@оо@лк@оц@ва'))
print(cleaned_str('сварка@@@@@лоб@ну@'))

# Задача_2
'''
Напишите программу, которая удаляет первые n символов из строки, и верните новую строку
'''
#
# def remove_str(str_,  number_char):
#     str_size = len(str_)
#     if number_char < str_size:
#         list_ = list(str_) # Преобразуем строку в список
#         list_ = list_[number_char:] # Удалили первые number_char символов
#         str_ = (''.join(list_)) # преобразуем список обратно в строку
#     else:
#         print('Введенное значение больше количества символов в строке')
#     return str_
#
# number_char = int(input('Введите количество удаляемых символов: '))
#
# str_ = 'sdlfjkhdasl fjhasdlkfjhasdlkjfhlk a'
#
# print(remove_str(str_, number_char))
#
