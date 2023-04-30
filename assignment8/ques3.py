#3.	Write a Python Program to Transpose a Matrix?

def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = [[0 for j in range(rows)] for i in range(cols)]
    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]
    return result

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

result = transpose_matrix(matrix)

for row in result:
    print(row)
