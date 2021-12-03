import matrix_implementations as m
import numpy as np

M1 = m.Matrix(4,4, np.array([-5, 8, -7, -10, -1, -1, 3, -5, -2, -9, 5, -10, 6, -2, 2, -10]).reshape(4,4))
M2 = m.Matrix(4,4, np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]).reshape(4,4))

print(m.tiled_multiplication(M1,M2,2))
