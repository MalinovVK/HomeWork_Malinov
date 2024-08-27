# def get_matrix(quantity, pair = 2, i=1, j=1):
#     print(f'Matrix {quantity}x{pair}:')
#     matr = [[0]*pair for i in range(quantity)]
#     for a in range(quantity):
#         for b in range(pair):
#             if i != 0:
#                 matr[a][b] = i
#                 i = 0
#             else:
#                 matr[a][b] = j
#     return matr

def quantity(first_num):
    quantity = 0
    for i in range(1, 20 + 1):
        for j in range(1, 20 + 1):
            if first_num % (i+j) == 0 and i != j:
                quantity += 1
    quantity_ = quantity/2
    quantity_ = int(quantity_)
    return quantity_


first_num = int(input("Введите число от 3 до 20: "))
while first_num < 3 or first_num > 20:
    print("Вы ввели неверное число")
    first_num = int(input("Введите число от 3 до 20: "))
pair = 2
matr = [0]*quantity(first_num)
k = -1
for i in range(1, 20 + 1):
    for j in range(1, 20 + 1):
        if first_num % (i+j) == 0 and i != j:
            if k < quantity(first_num)-1:
                k += 1
                matr[k] = str(i) + str(j)
            else:
                break
print(f'Количество пар чисел для {first_num}: {quantity(first_num)}')
print(matr)