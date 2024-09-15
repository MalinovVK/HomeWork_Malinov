import math
def divide(first, second):
    if second == 0:
        result = math.inf
    else:
        result = first/second
    return f'{first}/{second} = {result}'