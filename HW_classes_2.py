class House:
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


h1 = House('ЖК Эльбрус', 20)
h2 = House('ЖК Родина', 45)
print(h1)
print(h2)

print(h1 == h2)

h1 = h1 + 25
print(h1)
print(h2)
print(h1 == h2)

h2 += 10
print(h2)

print(h1 > h2)
print(h1 < h2)
print(h1 >= h2)
print(h1 <= h2)