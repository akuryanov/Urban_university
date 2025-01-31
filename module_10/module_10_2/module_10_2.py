# Домашнее задание по теме "Потоки на классах"

import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.warrior = 100

    def run(self):
        print('=======================================================')
        print(f'{self.name}, на нас напали!')
        print('=======================================================')
        day = 0
        while self.warrior != 0:
            self.warrior -= self.power
            time.sleep(1)
            day += 1
            print(f'{self.name} сражается {day} день(дня)..., осталось {self.warrior} воинов')
        print('=======================================================')
        print(f'{self.name} одержал победу спустя {day} дней (дня)!')
        print('=======================================================')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
print('Все битвы закончились!')
