# Домашнее задание по теме "Блокировки и обработка ошибок"

import threading
import time
from random import randint

class Bank(threading.Thread):
    def __init__(self):
        super().__init__()
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):

        for i in range(100):
            value = randint(50, 500)
            self.balance += value
            print(f'Пополнение: {value}. Баланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            time.sleep(0.01)

    def take(self):

        for i in range(100):
            value = randint(50, 500)
            print(f' Запрос на {value}')
            if self.balance >= value:
                self.balance -= value
                print(f'Снятие: {value}. Баланс: {self.balance}')

            else:
                print('Запрос отклонен. Недостаточно средств')
                self.lock.acquire()
            time.sleep(0.01)


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
