# Домашнее задание по теме "Очереди для обмена данными между потоками."

from queue import Queue
import threading
import time
import random

class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(threading.Thread):
    def __init__(self, guest):
        super().__init__()
        self.guest = guest

    def run(self):
        delay =  random.randint(3, 10)
        time.sleep(delay)

class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.queue = Queue()

    def guest_arrival(self, *guests: Guest):
        number_empty_table = len(tables)

        for i in range(len(guests)):
            if number_empty_table != 0:
                tables[i].guest = guests[i]
                number_empty_table -= 1
                guests[i].start()
                print(f'{guests[i].guest} сел(-а) за стол номер {tables[i].number}')
            else:
                self.queue.put(guests[i])
                print(f'{guests[i].guest} в очереди')

    def discuss_guests(self):
        while not self.queue.empty():
            for table in self.tables:
                if table.guest and not table.guest.is_alive():
                    print(f'{table.guest.guest} покушал(-а) и ушел(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
                if table.guest is None:
                    table.guest = self.queue.get()
                    print(f'{table.guest.guest} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    table.guest.start()


# Создание столов
tables = [Table(number) for number in range(1, 6)]

# Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
                'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
                ]
# Создание гостей
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(*tables)

# Приём гостей
cafe.guest_arrival(*guests)

# Обслуживание гостей
cafe.discuss_guests()