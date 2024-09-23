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

h1 = House('ЖК Эльбрус', 20)
h2 = House('ЖК Родина', 3)
h1.go_to(5)
h2.go_to(-1)
h1.go_to(24)