def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix


n = int(input('введите количество строк: '))
m = int(input('введите количество столбцов: '))
value = int(input('введите значение: '))
for s in get_matrix(n, m, value):
    print(s)
