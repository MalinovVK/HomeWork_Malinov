def add_everything_up(num, stroka):
    try:
        result = num + stroka
        result = round(result, 4)
    except TypeError:
        result = str(num) + str(stroka)
    finally:
        return result

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))