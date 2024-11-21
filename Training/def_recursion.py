# Факториал
# =================================================================
# def factorial(n):
#     if n <= 1:
#         return 1
#     else:
#         fact = n * factorial(n-1)
#         return fact
#
# print(factorial(1))
# print(factorial(2))
# print(factorial(3))
# print(factorial(4))
# =================================================================

# Сумма
# =================================================================
# def summation(n):
#     if n == 1:
#         return 1
#     else:
#         sum_ = n + summation(n-1)
#         return sum_
#
# print(summation(5))
# print(summation(6))
# print(summation(7))
# =================================================================

# Сумма чисел списка
# =================================================================
# def sum_odd(lst):
#     if len(lst) == 0:
#         return 0
#     else:
#         sum_odd_ = lst[0] + sum_odd(lst[1:])
#
#         return sum_odd_
#
#
# a = [1, 2, 3, 4, 5, 6, 7]
# print(sum_odd(a))
#
# a = [25]
# print(sum_odd(a))
#
# a = []
# print(sum_odd(a))
#
# a = [2, 8, 9, 7]
# print(sum_odd(a))
#
# =================================================================

# Сумма нечетных чисел от 1 до n
# =================================================================
# def func(n):
#     if n <= 0:
#         return 0
#     if n % 2 == 1:
#         return n + func(n - 2)
#     return func(n - 1)
#
# print(func(19))

# =================================================================

# Сумма нечетных чисел в списке
# =================================================================
# def sum_odd(lst):
#     sum_ = 0
#     if len(lst) == 0:
#         return 0
#     else:
#         for i in lst:
#             if i % 2 != 0:
#                 sum_ += i
#                 print(i)
#
#         return sum_
#
# a = [1, 2, 3, 4, 5, 6, 7]
# print(sum_odd(a))

# def sum_odd(lst):
#     global sum_
#     if len(lst) == 0:
#         return 0
#     else:
#         sum_odd(lst[1:])
#         if lst[0] % 2 != 0:
#             sum_ += lst[0]
#             return sum_
#
# sum_ = 0
# a = [1, 2, 3, 4, 5, 6, 7, 9, 7, 1]
# print('Сумма =', sum_odd(a))

# =================================================================

# Сумма нечётных чисел и вычитание чётных чисел
# =================================================================

# def sum_sub(lst):
#     global sum_
#     if len(lst) == 0:
#         return 0
#     else:
#         sum_odd(lst[1:])
#         if lst[0] % 2 != 0:
#             sum_ += lst[0]
#             return sum_
#         else:
#             sum_ -= lst[0]
#             return sum_
#
# sum_ = 0
# a = [1, 2, 3, 4, 5, 6, 7, 9, 7, 1]
# print('Сумма =', sum_sub(a))


# =================================================================

# Числа Фибоначчи
# =================================================================
def fib(n):
    f = []
    for i in range(n):
        f.append(i)

    for i in range(n):
        if i >= 2:
            f[i] = f[i-1] + f[i-2]
    return f

n = 10
print(fib(n))





