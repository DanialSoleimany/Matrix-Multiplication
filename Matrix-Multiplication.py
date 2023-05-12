import numpy as np

def dot(mat1, mat2):
    return np.dot(mat1, mat2)

A = [[1, 0], [0, 1]]
B = [[4, 1], [2, 2]]
AB = dot(A, B)

print(AB)
