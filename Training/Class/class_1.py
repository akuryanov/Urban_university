'''
Васильев А.Н. Программирование на Python в примерах и задачах
стр. 402 Задания для самостоятельной работы
№1

'''

class Alpha:
    def __init__(self, value_1, value_2):
        self.value_1 = value_1
        self.value_2 = value_2

    def get_value(self):
        print(f'Значение value_1 = {self.value_1}')
        print(f'Значение value_2 = {self.value_2}')

a = Alpha(23, 45)
a.get_value()
