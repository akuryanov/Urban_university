from threading import Event, Thread
import time

def first_worker():
    print('Первый рабочий приступил к своей задаче')
    event.wait() # Ожидание события
    print('Первый рабочий продолжил выполнять задачу')
    time.sleep(5)
    print('Первый рабочий закончил выполнять задачу')


def second_worker():
    print('Второй рабочий приступил к своей задаче')
    time.sleep(10)
    print('Второй рабочий закончил выполнять задачу')
    event.set() #

event = Event()  # Класс Event служит для синхронизации потоков между собой
thread1 = Thread(target=first_worker)
thread2 = Thread(target=second_worker)

thread1.start()
thread2.start()
