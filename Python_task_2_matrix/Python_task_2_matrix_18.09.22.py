
a, b, c = input('\nВведіть розмір матриці в форматі n*m: ')
matrix = []
mult = []
total = []
for i in range(int(a)):
    matrix_1 = []
    for j in range(int(c)):
        matrix_1.append(str(i*j))
    matrix.append(matrix_1)
print('\nВаша матриця:')
for i in range(int(a)):
    for j in range(int(c)):
        print(matrix[i][j].ljust(3), end=' ')
    print()
input('\nНажміть ENTER для виходу')

