from pprint import pprint
class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop():
    __file_name = 'products.txt'
    def get_products(self):
        file = open(self.__file_name, 'r')
        in_file = file.read()
        file.close()
        return in_file
    def add(self, *products):
        file = open(self.__file_name, 'a')
        for product in products:
            if product.__str__() in self.get_products():
                print(f'Продукт {product.__str__()} уже есть в магазине')
            else:
                file.write(f'{product.__str__()}\n')
        file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p1) # __str__
print(s1)
s1.add(p1, p2, p3)
print(s1.get_products())