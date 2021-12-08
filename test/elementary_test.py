import sys
#sys.path.append("/home/katarzyna/Documents/school/applied_algo/exam/TheMatrix")
sys.path.append("/home/gustavgyrst/Desktop/AA_Final/TheMatrix")
from matrix_implementations import *
import numpy as np

M1 = Matrix(4,4, np.array([-5, 8, -7, -10, -1, -1, 3, -5, -2, -9, 5, -10, 6, -2, 2, -10]).reshape(4,4))
M2 = Matrix(4,4, np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]).reshape(4,4))
C = Matrix(M1.rows(), M1.rows())

transpose(M2)

print("elementary normal:")
print(elementary_multiplication(M1,M2))

print("elementary transposed:")
print(elementary_multiplication_transposed(M1,M2))

print("elementary_write_through:")
print(elementary_multiplication_in_place(M1,M2,C))

#print(rec_matmul_write_through(M1,M2,C))