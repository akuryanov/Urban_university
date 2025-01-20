# Домашнее задание по теме "Многопроцессное программирование"

from datetime import datetime
import multiprocessing

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        line = file.readline()
        while line:
            line = file.readline()
            all_data.append(line)

filenames = [f'./file {number}.txt' for number in range(1, 5)]

start_time = datetime.now()
for filename in filenames:
    read_info(filename)

end_time = datetime.now()
print(f'Линейный вызов, время выполнения - {end_time - start_time}')


start_time = datetime.now()
if __name__ == '__main__':

    with multiprocessing.Pool(4) as p:
        p.map(read_info, filenames)

end_time = datetime.now()
print(f'Многопроцессный вызов, время выполнения - {end_time - start_time}')
