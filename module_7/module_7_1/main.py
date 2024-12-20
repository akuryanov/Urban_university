class Product:
   def __init__(self, name, weight, category):
       self.name = name
       self. weight = weight
       self.category = category

   def __str__(self):
       return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'product.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        print(file.read())
        file.close()

    def add(self, *product):
        file = open(self.__file_name, 'a+')
        file.seek(0)

        content = file.read()

        for value in product:
            if str(value.name) in content:
                print(f'Продукт {value.name} уже есть в магазине')
            else:
                print(value)
                file.write(str(value) + '\n')
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)

print(s1.get_products())


