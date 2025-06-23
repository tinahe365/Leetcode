def matrixTranspose(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    result = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range (cols):
            result[j][i] = matrix[i][j]

    return result

def matrixTranspose2(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    result = [[matrix[j][i] for j in range(rows)] for i in range(cols)]
    return result


