def calculate_structure_sum(object):
    summ = 0
    for i in range(len(object)):
        if isinstance(object[i], list):
            summ += sum(object[i])
        if isinstance(object[i], dict):
            summ += sum(object[i].values())
            for key in object[i].keys():
                summ += len(key)
        if isinstance(object[i], str):
            summ += len(object[i])
        if isinstance(object[i], tuple):
            for j in range(len(object[i])):
                if isinstance(object[i][j], int):
                    summ += object[i][j]
                elif isinstance(object[i][j], str):
                    summ += len(object[i][j])
                else:
                    summ += sum(object[i][j].values())
                    for key in object[i][j].keys():
                        summ += len(key)
    return print(f'Сумма всех элементов: {summ}')

data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]

data_structure_1 = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello"] #Без: ((), [{(2, 'Urban', ('Urban2', 35))}])]

calculate_structure_sum(data_structure_1)