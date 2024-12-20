import io
from pprint import pprint

name = 'sample.txt'
file = open(name, 'r') # r - (read) чтение, w - (write) запись, a - (append) добавление
print(file)
pprint(file.read()) # Просмотр содержимого файла
file.close()

name = 'sample2.txt'
file = open(name, 'w') # При открытии файла в режиме записи старая информация заменяется на новую
                       # Если файл не будет найден, он будет создан
file.write('hello')
file.close()

file = open(name, 'a')
file.write('\nhello World')
file.close()

name = 'sample.txt'
file= open(name, 'r')
print(file.tell()) # Позиция курсора
pprint(file.read())
print(file.tell()) # Позиция курсора
print(file.seek(15)) # Установить позицию курсора
pprint(file.read())
file.close()