def get_matrix(n, m, value):
    matrix = []
    if n and m > 0:
        for i in range(n):
            matrix.append([])
            for j in range(m):
                matrix[i].append(value)
    else:
        matrix = []
    print(matrix)

get_matrix(5,3, 5)
get_matrix(0, 8, 5)
get_matrix(5,0, 5)
get_matrix(5,-1, 5)
get_matrix(-1, 4, 5)