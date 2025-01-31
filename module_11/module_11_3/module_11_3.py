import inspect
from pprint import pprint

class Introspection:
    def __init__(self, obj):
        self.obj = obj
        self.result = {}

    def __str__(self):
        return f'{self}'

    def introspection_info(self):

        # Получаем тип объекта
        type_ = type(self.obj).__name__

        # Получаем все атрибуты объекта
        attr_ = dir(self.obj)

        # Получаем список методов
        methods = [method[0] for method in inspect.getmembers(self.obj)]

        # Получаем имя модуля к которому принадлежит объект
        module = self.obj.__class__.__module__

        self.result = {
                       'type' : type_,
                       'attributes' : attr_,
                       'methods' : methods,
                       'module' : module,

                       }

        return self.result

if __name__ == '__main__':
    introspection = Introspection('Объект')
    pprint(introspection.introspection_info())



