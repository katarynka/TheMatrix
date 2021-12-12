import numpy as np
import sys
sys.path.append("/home/katarzyna/Documents/school/applied_algo/exam/TheMatrix")
from matrix_implementations import *

M1 = Matrix(4,4, np.array([-5, 8, -7, -10, -1, -1, 3, -5, -2, -9, 5, -10, 6, -2, 2, -10]).reshape(4,4))
M2 = Matrix(4,4, np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]).reshape(4,4))


# print(m.tiled_multiplication2(M1,M2,2))
print(tiled_multiplication(M1,M2,2))
print("exp")
print(np.matmul(np.array([-5, 8, -7, -10, -1, -1, 3, -5, -2, -9, 5, -10, 6, -2, 2, -10]).reshape(4,4),np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]).reshape(4,4)))

# res = 1.0/3.0
# print(res)
# print(type(res))

# res2 = 0.0928349287459834759384759348759384579384759834

# print(res2)

# print(type(res2))

# print(len(str(res)))

# print(len('09283492874598348'))

# res3 = 2093482058024958093458390485.30230123490234

# print(res3)

# print(len('093482058024958'))

# res4 = 9007199254740992 + 1

# #Here you see that it will round off to even numbers
# res5 = 18014398509481985.00000000000000

# print(res5)
