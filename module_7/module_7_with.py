import io
from pprint import pprint

name = 'sample.txt'
# file = open(name, 'r', encoding='utf-8')

with open(name, encoding='utf-8') as file: # Пока открыт файл...
    for line in file:
        # for char in line:
        #     print(char)
        print(line, end='')


# При использовании with нет необходимости закрывать файл, так как после окончания работы with файл будет закрыт
