# Динамическая типизация
# В Python тип хранится не в переменной, а в самом объекте
# А сама переменная ссылается на объект
# В Python всё является объектом

name = "Urban"
print(name, type(name))

name = 5
print(name, type(name))

name = 5.5
print(name, type(name))

name = [1, 2]
print(name, type(name))

# Переменные ДЗ

number_of_completed_homeworks = 12
number_of_hours_spent = 1.5
course_name = 'Python'
time_for_one_task = number_of_hours_spent / number_of_completed_homeworks

print('Курс:', course_name,', всего задач:', number_of_completed_homeworks,', затрачено:',
      number_of_hours_spent, ', среднее время выполнения', time_for_one_task)

