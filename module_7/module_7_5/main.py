import os
import time
current_path = os.getcwd()

for root, dirs, files in os.walk(current_path):

    # root - строка вершина каталога
    # dirs - список вложенных каталогов
    # files - список файлов в каталоге
    for file in files:
        filepath = f'{os.path.join(root)}/{file}'
        parent_dir = os.path.dirname(root)
        filetime = os.path.getmtime(root)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filename = f'{root}/{file}'
        file_size = os.path.getsize(filename)
        print(f'Обнаружен файл: {file}\n Путь: {filepath}\n Родительская директория: {parent_dir}\n Время изменения: {formatted_time}\n Размер: {file_size} байт\n')