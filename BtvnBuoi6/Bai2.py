import numpy as np


def transpose (matrix :list, a : int, b : int):
    for i in range(a):
        for j in range(b):
            print(matrix[j][i], end=' ')
matrix = np.array([[1,2,3],[4,5,6],[7,8,9],])
transpose_matrix = np.transpose(matrix)
print(transpose_matrix)
