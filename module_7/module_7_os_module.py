import os

print(f'Текущая директория {os.getcwd()}') # выводим путь рабочей директории
if os.path.exists('second'): # Если директория second существует
    os.chdir('second') # открываем ее для изменения
else:
    os.mkdir('second') # Создаем новую папку second
    os.chdir('second')  # и открываем ее для изменения
print(f'Текущая директория {os.getcwd()}') # выводим путь рабочей директории

# Если необходимо создать несколько вложенных папок
# os.makedirs(r'third/fourch')
os.chdir('/home/akuryanov/DOC/Python обучение/Urban_University/Urban_Universiry/module_7')
print(f'Текущая директория {os.getcwd()}') # выводим путь рабочей директории
file = [f for f in os.listdir() if os.path.isfile(f)]  # создание списка файлов
dirs = [d for d in os.listdir() if os.path.isdir(d)] # создание списка директорий

print(dirs)
print(file)

print(os.stat(file[2])) # Получение информации о файле

os.system('pip install random2') # вызов файла в консоли
