class Car:
    def __init__(self, model: str, __vin: int, __numbers: str):
        self.model = model
        self.__vin = __vin
        self.__numbers = __numbers
        self.__is_valid_vin(__vin)
        self.__is_valid_numbers(__numbers)

    def __is_valid_vin(self, vin_number):
        if (type(vin_number) != int) or (vin_number < 1000000 or vin_number > 9999999):
            raise IncorrectVinNumber
        else:
            return True

    def __is_valid_numbers(self, vin_number):
        if (isinstance(vin_number, str) != True) or (len(vin_number) != 6):
            raise IncorrectCarNumbers
        else:
            return True
class IncorrectVinNumber(Exception):
    message = 'Неверный диапазон для vin номера'
class IncorrectCarNumbers(Exception):
    message = 'Неверная длина номера'

try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')

