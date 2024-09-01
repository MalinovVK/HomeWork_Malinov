def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
# print_params(4, 3, 5, 8)
# print_params(c = [1,2,3])

values_list = [1,10,15]
values_dict = {'a': 3, 'b': 'Privet', 'c': True}

print_params(*values_dict.items())
print_params(**values_dict)

values_list_2 = [3.14, 'Urban']
print_params(*values_list_2)