# Декораторы - это обертка вокруг функций (или классов), которая меняет способ работы этой функции
# Разработчик может писать свой код так, как ему хочется,
# и использовать декораторы только для расширения функциональности.
# Это функция, которая принимает л=другую функцию, в качестве аргумента и возвращает третью

# Создание декоратора
# Вариант 1
# def null_decorator(func):
#     return func
#
# def greet():
#     return 'Hello!'
#
# greet = null_decorator(greet)
#
# print(greet())
#
# # Вариант 2
# def null_decorator(func):
#     return func
# @null_decorator
# def greet():
#     return 'Hello!'
# print(greet())
#
# # Вариант 3 определение функции на лету внутри декоратора
#
# def uppercase(func):
#     def wrapper():
#         original_result = func()
#         modified_result = original_result.upper()
#         return modified_result
#     return wrapper
#
# @uppercase
# def greet():
#     return 'Hello!'
#
# print(greet())

# =================================================================
# Практика
# =================================================================

# 1 - написать функцию, которая возвращает функцию повторения двух первых символов n раз
# 2 - создать массив функций и применить все функции поочередно к аргументу
# 3 - применить все функции поочередно к массиву аргументов

# 1
animal = 'мишка'
animals = ['зайка', 'мишка', 'бегемотик']

def gen_repeat(n):
    def repeat(animal):
        return (animal[:2] + '-') * n + animal
    return repeat

test1 = gen_repeat(1)
test2 = gen_repeat(2)
print(test1(animal))
print(test2(animal))

# 2
repetition = [gen_repeat(n) for n in range(1, 4)]
result = [func(animal) for func in repetition]
print(result)

# 3
fin_result = [func(x) for func in repetition for x in animals]
print(fin_result)


