'''
Васильев А.Н. Программирование на Python в примерах и задачах
стр. 402 Задания для самостоятельной работы
№3

'''
class Alpha:
    def __init__(self, *args):
        self.args = list(*args)
        self.list_ = []

    def get_list(self):
        for i in self.args:
            if isinstance(i, int):
                self.list_.append(i)
        return self.list_

    def average(self):
        return sum(self.list_) / len(self.list_)

list_ = [1, 2, 'r', 1, (1, 2, 3), 1, 3.4, 5]

a = Alpha(list_)
print(type(a.args))

print(a.get_list())
print(a. average())

