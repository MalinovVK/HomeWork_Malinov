def divide(first, second):
    if second == 0:
        result = "Ошибка"
    else:
        result = first/second
    return f'{first}/{second} = {result}'
