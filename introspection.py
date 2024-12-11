import inspect
from pprint import pprint


class Human:
    years = 21
    gender = 'male'

    def __init__(self, name):
        self.name = name
        Human.hello(self)

    def hello(self):
        print('hello!\nMy name is Vlad')


def introspection_info(obj):
    list_info = {}
    dir_obj = dir(obj)
    print('   Выберите:\n'
          ' - Тип объекта. Нажмите: "T"\n',
          '- Атрибуты объекта. Нажмите: "A"\n',
          '- Методы объекта. Нажмите: "M"\n',
          '- Модуль, к которому объект принадлежит. Нажмите: "Mo"\n',
          f'- Прекратить - нажмите "B"\n')
    while True:
        a = input('eng: ')
        if a == 'T':
            list_info['type'] = type(obj).__name__
        elif a == 'A':
            dir_put = []
            for i in dir(obj):
                if not callable(getattr(obj, i)):
                    dir_put.append(i)
            list_info['attributes'] = dir_put
        elif a == 'M':
            methods = [method for method in dir(obj) if callable(getattr(obj, method))]
            list_info['methods'] = methods
        elif a == 'Mo':
            if hasattr(obj, '__module__'):
                list_info['module'] = obj.__module__
        elif a == 'B':
            break
    return list_info


p1 = Human("vlad")
p1_info = introspection_info(p1)
pprint(p1_info)
