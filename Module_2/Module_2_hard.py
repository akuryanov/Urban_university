import random

result = ''

a = ''
first_fild = random.randint(3, 20) # генерируем случайное целое число от 3 до 20 для первого поля
print('Число в первом поле: ', first_fild)
for i in range(1, first_fild):
    for j in range(i, first_fild):
        if i != j:
            if first_fild % (i + j) == 0:
                a = str(i) + str(j)
                print(a)
                result += a

print(result)
while True:
    pass

