#2.	Write a Python Program to Multiply Two Matrices?


def multiply_matrices(matrix1, matrix2):
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])
    if cols1 != rows2:
        return None
    result = [[0 for j in range(cols2)] for i in range(rows1)]
    for i in range(rows1):
        for j in range(cols2):
            for k in range(rows2):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result

matrix1 = [[1, 2, 3],
           [4, 5, 6]]

matrix2 = [[7, 8],
           [9, 10],
           [11, 12]]

result = multiply_matrices(matrix1, matrix2)

for row in result:
    print(row)
