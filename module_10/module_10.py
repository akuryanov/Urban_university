# Потоки

import threading
import time

def func1():
    for i in range(10):
        time.sleep(1)
        print(i, threading.current_thread())


def func2():
    for i in range(10):
        time.sleep(1)
        print(i, threading.current_thread())
        # print(threading.current_thread().is_alive())

thread = threading.Thread(target=func2)
thread.start()
thread.join()
print(thread.is_alive())
func1()

print(threading.enumerate()) # Список потоков
print(threading.current_thread()) #