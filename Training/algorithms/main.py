# Числа Фибоначчи
# =================================================================
# По заданному числу n вывести n-e число Фибоначчи 0 < n < 90

n = int(input('Введите целое число: '))
f = [0, 1]

while len(f) <= n:
    f.append(f[-1] + f[-2])
l = ' '.join(map(str,f)) # map(str, f) переводит значения типа int в str
print((f'Последовательность Фибоначи для {n} элементов : {l}'))


#  Путь до ксерокса
# =================================================================

# n = int(input('Введите этаж '))
# k = int(input('введите этаж ксерокса '))
#
# i = max(n // k, 1)
# ans1 = abs(n - k*i)
# i += 1
# ans2 = abs(n - k*i)
#
# print(min(ans1, ans2))