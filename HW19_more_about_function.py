data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]
def calculate_structure_sum(object):
    summ = 0
    if isinstance(object,(int, float)):
        summ += object
    if isinstance(object, str):
        summ += len(object)
    elif isinstance(object, (list, tuple, set)):
        for item in object:
            summ += calculate_structure_sum(item)
    elif isinstance(object, dict):
        for key, value in object.items():
            summ += calculate_structure_sum(key)
            summ += calculate_structure_sum(value)
    return summ

print(calculate_structure_sum(data_structure))