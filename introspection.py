
from pprint import pprint
def introspection_info(obj):
    list_info = []
    print('   Выберите:\n'
          ' - Тип объекта. Нажмите: "T"\n',
          '- Атрибуты объекта. Нажмите: "A"\n',
          '- Методы объекта. Нажмите: "M"\n',
          '- Модуль, к которому объект принадлежит. Нажмите: "Mo"\n',
          f'- Прекратить - нажмите "B"\n')
    while True:
        a = input('eng: ')
        if a == 'T':
            list_info.append(type(obj))
        elif a == 'A':
            list_info.append(dir(obj))
        elif a == 'M':
            list_info.append()
        elif a == 'Mo':
            list_info.append()
        elif a == 'B':
            break
    return list_info

number_info = introspection_info(42)
pprint(number_info)
