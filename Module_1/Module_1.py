
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = tuple(students)
students = sorted(students)

grades_ = []

i = 0
for i in range(len(grades)):
    grades_.append (sum(grades[i]) / len(grades[i]))

dict_ = zip(students, grades_) # Создает пару Ключ:Значение
dict_ = dict(dict_)
print(dict_)