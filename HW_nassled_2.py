class Vehicle:
    __COLOR_VARIANTS = ['blue', 'green', 'grey', 'red']
    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(f' {self.get_model()}', '\n', self.get_horsepower(), '\n', self.get_color(), '\n', f'Владелец: {self.owner}')

    def set_color(self, new_color: str):
        if new_color.lower() in Vehicle.__COLOR_VARIANTS:
            self.__color = new_color.lower()
            self.print_info()
        else:
            print(f' Нельзя сменить цвет на {new_color}')
class Sedan(Vehicle):
    pass


vehicle1 = Sedan('Malinov', 'Mazda MX-5', 184, 'grey')
vehicle1.print_info()
print('')
vehicle1.set_color('purple')
vehicle1.owner = 'Ivanov'
print('')
vehicle1.set_color('RED')