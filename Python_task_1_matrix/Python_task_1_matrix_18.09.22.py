
n, k, m = input('\nВведіть розмір матриці у форматі n*n: ')
print()
matrix = []
count = 1
for i in range(int(n)):
    matrix_1 = []
    for j in range(int(m)):
        if count != 3:
            matrix_1.append(input(f'Введіть {count}-е слово для матриці: '))
        else:
            matrix_1.append(input(f'Введіть {count}-є слово для матриці: '))
        count += 1
    matrix.append(matrix_1)

print('\nВаша матриця:')
for i in range(int(n)):
    for j in range(int(m)):
        print(matrix[i][j], end=' ')
    print()
input('\nPress ENTER to exit') 
