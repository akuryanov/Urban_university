class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                print(i)
    def __len__(self):
        return self.number_of_floors

    # def __str__(self): # Для вариантов вывода 1 и 2
    #     return self.name

    def __str__(self): # Для варианта вывода 3
        return f'Название: {self.name}, количество этажей {self.number_of_floors}'

# h1 = House('ЖК Горский', 18)
# h2 = House('Домик в деревне', 2)
#
# h1.go_to(5)
# h2.go_to(10)

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# Вариант вывода 1
# print(f'{h1.name}, количество этажей {h1.number_of_floors}')
# print(f'{h2.name}, количество этажей {h2.number_of_floors}')

# Вариант вывода 2
# print(f'{str(h1)}, количество этажей {len(h1)}')
# print(f'{str(h1)}, количество этажей {len(h1)}')

# Вариант вывода 3
print(h1)
print(h2)
print(len(h1))
print(len(h2))