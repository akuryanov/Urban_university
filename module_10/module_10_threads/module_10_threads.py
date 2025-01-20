# Очереди в потоках

from queue import Queue
import time

import threading


def getter(queue):
    while True:
        time.sleep(5)
        item = queue.get()
        print('Взят элемент', item)

q = Queue() # Создание очереди
thread1 = threading.Thread(target=getter, args=(q, ),  daemon=True)
thread1.start()

for i in range(10):
    time.sleep(2)
    q.put(i)
    print(threading.currentThread(), 'положил в очередь элемент', i)
