# Декораторы - это обертка вокруг функций (или классов), которая меняет способ работы этой функции
# Разработчик может писать свой код так, как ему хочется,
# и использовать декораторы только для расширения функциональности.
# Это функция, которая принимает л=другую функцию, в качестве аргумента и возвращает третью

# Создание декоратора
# Вариант 1
def null_decorator(func):
    return func

def greet():
    return 'Hello!'

greet = null_decorator(greet)

print(greet())

# Вариант 2
def null_decorator(func):
    return func
@null_decorator
def greet():
    return 'Hello!'
print(greet())

# Вариант 3 определение функции на лету внутри декоратора

def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper

@uppercase
def greet():
    return 'Hello!'

print(greet())