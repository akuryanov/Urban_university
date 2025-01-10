class  IncorrectVinNumber (Exception):
    def __init__(self, message):
        self.message = message

class IncorrectCartNumber(Exception):
    def __init__(self, message: str):
        self.message = message

class Car:
    def __init__(self, model, __vin, __numbers):
        self.model = model
        if self.__is_valid_vin(__vin):
            self.vin = __vin

        if self.__is_valid_number(__numbers):
            self.numbers = __numbers

    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        elif len(str(vin_number)) != 7:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        else:
            return True

    def __is_valid_number(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectCartNumber('Некорректный тип данных для номера')
        elif len(numbers) != 6:
            raise IncorrectCartNumber('Неверная длина номера')
        else:
            return True



try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCartNumber as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCartNumber as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCartNumber as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')