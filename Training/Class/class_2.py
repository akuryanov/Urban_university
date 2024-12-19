'''
Васильев А.Н. Программирование на Python в примерах и задачах
стр. 402 Задания для самостоятельной работы
№2

'''

class Alpha:
    def __init__(self, var_1, var_2):
        self.var_1 = var_1
        self.var_2 = var_2

        if isinstance(self.var_1, str) and isinstance(self.var_2, str) or \
                isinstance(self.var_1, int) and isinstance(self.var_2, int):
            var = self.var_1 + self.var_2
            return print(var)

a = Alpha('2', '4')
a = Alpha(2, 4)
a = Alpha('2', 4)
a = Alpha(2, 4.0)
