import random

result = ''
first_fild = random.randint(3, 20) # генерируем случайное целое число от 3 до 20 для первого поля
print('Число в первом поле: ', first_fild)

for i in range(1, first_fild):
    for j in range(i, first_fild):
        if i != j:
            if first_fild % (i + j) == 0:
                pair_of_number = str(i) + str(j)
                result += pair_of_number


print(result)

