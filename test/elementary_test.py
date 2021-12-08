import sys
#sys.path.append("/home/katarzyna/Documents/school/applied_algo/exam/TheMatrix")
sys.path.append("/home/gustavgyrst/Desktop/AA_Final/TheMatrix")
from matrix_implementations import *
import numpy as np


# M1 = Matrix(4,4, np.array([-5, 8, -7, -10, -1, -1, 3, -5, -2, -9, 5, -10, 6, -2, 2, -10]).reshape(4,4))
# M2 = Matrix(4,4, np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]).reshape(4,4))
# print(M2)
# transpose(M2)
# print(M2)
# t1 = np.array([-5, 8, -7, -10, -1, -1, 3, -5, -2, -9, 5, -10, 6, -2, 2, -10]).reshape(4,4)
# t2 = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]).reshape(4,4)
# print(elementary_multiplication(M1,M2))
# transpose(M2)
# print(elementary_multiplication_transposed(M1,M2))
# print("expected")
# print(np.matmul(t1,t2))
# t3 = np.array([-5,8,-1,-1]).reshape(2,2)
# t4 = np.array([1,2,5,6]).reshape(2,2)
# test11 = np.matmul(t3,t4)
# t5 = np.array([-7,-10,3,-5]).reshape(2,2)
# t6 = np.array([9,10,13,14]).reshape(2,2)
# test12 = np.matmul(t5,t6)
# print("#1")
# print(np.add(test11,test12))

M1 = Matrix(4,4, np.array([-5, 8, -7, -10, -1, -1, 3, -5, -2, -9, 5, -10, 6, -2, 2, -10]).reshape(4,4))
M2 = Matrix(4,4, np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]).reshape(4,4))
C = Matrix(M1.rows(), M1.rows())


transpose(M2)

print(elementary_multiplication(M1,M2))


print(elementary_multiplication_in_place(M1,M2,C))
