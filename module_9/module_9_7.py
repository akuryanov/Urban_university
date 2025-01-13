# Домашнее задание по теме "Декораторы"
from math import sqrt

def is_prime(func):
    def wrapper(a, b, c):
        sum_ = func(a, b, c)
        i = 2
        flag = True
        while i <= sqrt(sum_):
            if sum_ % i == 0:
                flag = False
                break
            i += 1
        if flag:
            return 'Простое'
        else:
            return 'Составное'
    return wrapper

@is_prime
def sum_three(a, b, c):
    sum_ = a + b + c
    print(sum_)
    return sum_


result = sum_three(4, 3, 4)
print(result)
result = sum_three(2, 3, 4)
print(result)
