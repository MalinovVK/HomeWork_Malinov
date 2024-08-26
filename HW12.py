def get_matrix(str, column, value):
    print(f'Matrix {str}x{column}:')
    matr = [[0]*column for i in range(str)]
    for i in range(str):
        for j in range(column):
            matr[i][j] = value
        print(matr[i])
    print('')
    return matr

get_matrix(3,3,10)
get_matrix(2,4,2)
get_matrix(4,3, 5)
