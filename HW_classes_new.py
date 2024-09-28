class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    def __init__(self, name, numbers_of_floors):
        self.name = name
        self.numbers_of_floor = numbers_of_floors


    def go_to(self, new_floor):
        if new_floor > self.numbers_of_floor or new_floor < 1:
            print(f'Этаж: {new_floor} - Такого этажа не существует в {self.name}')
        else:
            for i in range(1, new_floor+1):
                print(f'{i}')
            print(f'Добро пожаловать, вы на {new_floor}')

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.numbers_of_floor}'
    def __len__(self):
        print(self.numbers_of_floor)
    def __eq__(self, other):
        return self.numbers_of_floor == other
    def __lt__(self, other):
        return self.numbers_of_floor < other
    def __le__(self, other):
        return self.numbers_of_floor <= other
    def __gt__(self, other):
        return self.numbers_of_floor > other
    def __ge__(self, other):
        return self.numbers_of_floor >= other
    def __ne__(self, other):
        return self.numbers_of_floor != other
    def __add__(self, value):
        self.numbers_of_floor = self.numbers_of_floor + value
        return self

    def __del__(self):
        self.houses_history.append(self.name)
        return print(f'{self.name} снесен, но остается в истории')

h1 = House('ЖК Эльбрус', 20)
h2 = House('ЖК Родина', 45)
h3 = House('ЖК Восток', 12)
del h3
del h2
print(f'Список снесенных домов: {House.houses_history}')
del h1
print(f'Список снесенных домов: {House.houses_history}')