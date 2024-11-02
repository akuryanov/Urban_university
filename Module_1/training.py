# Задачи по теме "Работа со строками"

# Задача_1
'''Напишите функцию search_substr(subst, st), которая принимает 2 строки и определяет,
имеется ли подстрока subst в строке st. В случае нахождения подстроки,
возвращается фраза «Есть контакт!», а иначе «Мимо!».
Должно быть найдено совпадение независимо от регистра обеих строк.'''

def search_substr(subctr, str):
    if subctr in str:
        return('Есть контакт!')
    else:
        return ('Мимо!')

str = 'которая принимает 2 строки и определяет'
subctr = 'определяет'
output_str = search_substr(subctr, str)
print(output_str)
subctr = 'много'
output_str = search_substr(subctr, str)
print(output_str)
