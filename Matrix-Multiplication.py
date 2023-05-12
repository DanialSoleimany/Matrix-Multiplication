import numpy as np

def dot(mat1, mat2):
    return np.dot(mat1, mat2)

mat1 = [[1, 0], [0, 1]]
mat2 = [[4, 1], [2, 2]]

print(dot(mat1, mat2))