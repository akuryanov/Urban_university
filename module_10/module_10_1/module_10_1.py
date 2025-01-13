# Домашнее задание по теме "Создание потоков"

import threading
from datetime import datetime
import time



def wite_words(word_count, file_name):
    with open(file_name, 'w' , encoding='utf-8') as file:
        for i in range(1, word_count+1):
            file.write('Какое-то слово № ' + str(i) + '\n')
            time.sleep(0.1)
    return print(f'Завершилась запись в файл {file_name}')


start_time = datetime.now()

example = {10: 'example1.txt',
           30: 'example2.txt',
           200: 'example3.txt',
           100: 'example4.txt'}
for word_count, file_name in example.items():
    wite_words(word_count, file_name)

end_time = datetime.now()
execution_time = end_time - start_time
print(f'Работа потоков {str(execution_time)}')


start_time = datetime.now()
thread1 = threading.Thread(target=wite_words, args=(10, 'example5.txt'))
thread2 = threading.Thread(target=wite_words, args=(30, 'example6.txt'))
thread3 = threading.Thread(target=wite_words, args=(200, 'example7.txt'))
thread4 = threading.Thread(target=wite_words, args=(100, 'example8.txt'))
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread1.join()
thread2.join()
thread3.join()
thread4.join()

end_time = datetime.now()
execution_time = end_time - start_time
print(f'Работа потоков {str(execution_time)}')



