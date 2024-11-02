'''Словари и множества'''
# Словари являются изменяемой структурой
# phone_book = {'Denis': 88008888888, 'Alex': 88008877777} # Словари имеют связи - ключ: значение
# print(phone_book)
# print(phone_book['Denis'])
#
# phone_book['Denis'] = 88009999999 # Можно изменять элементы словаря
# print(phone_book)
#
# phone_book['Anton'] = 88005553555 # Можно добавлять элементы словаря
# print(phone_book)
#
# del phone_book['Alex'] # Можно удалять элементы словаря
# print(phone_book)
#
# phone_book.update({'Max': 88009651213,
#                    'Sasha': 880074532132}) # Изменение нескольких элементов
# print(phone_book)
#
# print(phone_book.get('Kamla', 'Такого ключа нет'))
# print(phone_book)
# a = phone_book.pop('Anton') # Вырезает элемент из словаря, при этом сохраняет значение указанного ключа
# print(a)
# print(phone_book)
#
# print(phone_book.keys())
# print((phone_book.values()))
# print(phone_book.items())
#
# # Множества не содержат повторяющиеся элементы
#
# set_ = {1, 2, 4, 5, 8, 8, 5 ,5 ,8 ,8 ,1 ,3 ,7, 'String', True, (1, 2 ,3)}
# print(set_)
#
# # Списки можно превратить в множества
# list_ = [1, 2, 4, 5, 8, 8, 5 ,5 ,8 ,8 ,1 ,3 ,7, 'String', True, (1, 2 ,3)]
# print(list_)
# print(set(list_))
# print(set_.discard(1)) # Если элемент не найден в множестве, ошибка выводиться не будет
# print(set_)
# print(set_.remove(2))
# print(set_)
# print(set_.add(6))
# print(set_)

'''ДЗ'''

my_dict = {'Alex': 1998, 'Lisa':2001, 'Max': 2016}
print(my_dict)
print(my_dict['Max'])
print(my_dict.get('Nina', 'Такой ключ отсутствует в словаре'))
my_dict.update({'Nina': 2005,
                'Artur': 2004})
print(my_dict)
print(my_dict.pop('Lisa'))
print(my_dict)


my_set = {1, 2, 4, 5, 8, 8, 5 ,5 ,8 ,8 ,1 ,3 ,7, 'String', True, (1, 2 ,3)}
print(my_set)
my_set.add('None')
my_set.add(58)
print(my_set)
my_set.discard((1, 2, 3))
print(my_set)
