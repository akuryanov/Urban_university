# Итераторы
# import sys
# from itertools import repeat
#
# ex_iterator = repeat('4', 100_000)
# print(ex_iterator)
# print(f'Размер итератора - {sys.getsizeof(ex_iterator)}')
#
# ex_str = '4'* 100_000
# print(f'Размер списка - {sys.getsizeof(ex_str)}')

# class Iter:
#
#     def __init__(self):
#         self.first = 'Первый элемент'
#         self.second = 'Второй элемент'
#         self.third = 'Третий элемент'
#         self.i = 0
#
#     def __iter__(self):
#         # обнуляем счетчик перед циклом
#         self.i = 0
#         # Возвращаем ссылку на себя, так как сам объект должен быть итератором
#         return self
#
#     def __next__(self):
#         # Этот метод возвращает значения по требованию python (ленивые вычисления)
#         self.i += 1
#         if self.i == 1:
#             return self.first
#         if self.i == 2:
#             return self.second
#         if self.i == 3:
#             return self.third
#         if self.i == 4:
#             return 'Подсчет окончен'
#         raise StopIteration() # признак того, что больше возвращать нечего
#
# obj = Iter()
# print(obj)
# for value in obj:
#     print(value)
#
# # Итератор вызывает метод __next__ при каждом проходе цикла
# # Если в __next__ возникает исключение StopIteration() - то значит в объекте больше нет элементов, цикл прекращается
#
# # =========================================================================
# # Числа Фибоначчи
# # =========================================================================
#
class Fibonacci:

    def __init__(self, n):
        self.i = 0
        self.a = 0
        self.b = 1
        self.n = n

    def __iter__(self):
        self.i = 0
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        self.i += 1
        if self.i > 1:
            if self.i > self.n:
                raise StopIteration()
            self.a, self.b = self.b, self.a + self.b
        return self.a

fib_iterator = Fibonacci(20)
print(fib_iterator)
fib = []
for value in fib_iterator:
    fib.append(value)
print(' '.join(map(str, fib)))