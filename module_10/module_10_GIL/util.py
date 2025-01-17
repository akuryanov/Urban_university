import datetime
import json
from random import randint

res = []
files = ['file1.json', 'file2.json', 'file3.json', 'file4.json']

# Запись данных в файлы

# for file in files:
#     for _ in range(100_000):
#         res.append(randint(0, 10000)) # Генерируем случайное число и добавляем в список res
#     with open(file, 'w') as f:
#         json.dump(res, f) # Передаем список в файл
#     res = []

# Чтение данных из файлов и суммирование всех данных

res_to_count = []
start = datetime.datetime.now()

for file in files:
    with open(file, 'r') as f:
        data = json.load(f) # Читаем список из файла
        res_to_count.extend(data) # Добавляем полученный список в список res_to_count

print(sum(res_to_count))

end = datetime.datetime.now()

print(end - start)