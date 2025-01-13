# Потоки
#
import threading
import time

from gevent.libev.watcher import timer


# Можно создавать потоки используя класс threading.Thread
#
# def func1():
#     for i in range(10):
#         time.sleep(1)
#         print(i, threading.current_thread())
#
#
# def func2():
#     for i in range(10):
#         time.sleep(1)
#         print(i, threading.current_thread())
#         # print(threading.current_thread().is_alive())
#
# thread = threading.Thread(target=func2)
# thread.start()
# thread.join()
# print(thread.is_alive())
# func1()
#
# print(threading.enumerate()) # Список потоков
# print(threading.current_thread()) #

# Можно создать свой класс

class MyThread(threading.Thread):
    def __init__(self, name, counter, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.counter = counter
        self.delay = delay


    def timer(self, name, counter, delay):
        while counter:
            time.sleep(delay)
            print(f'{name} {time.ctime(time.time())}')
            counter -= 1

    def run(self):
        print(f'Поток {self.name} запущен')
        self.timer(self.name, self.counter, self.delay)

        print(f'Поток {self.name} завершен')


thread1 = MyThread('thread1', 5, 1)
thread2 = MyThread('thread2', 3, .5)
thread1.start()
thread2.start()