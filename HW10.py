my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
print(my_list)
i = 0
while True:
    if i < len(my_list):
        if my_list[i] > 0:
            print(my_list[i])
        # if my_list[i] == 0:
        #     print(f'{my_list[i]} Число не является ни положительным, не отрицательным')
        if my_list[i] < 0:
            break
        i += 1


    