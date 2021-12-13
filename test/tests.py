import random
from typing import List
import numpy as np
import sys
#sys.path.append("/home/katarzyna/Documents/school/applied_algo/exam/TheMatrix")
sys.path.append("/home/gustavgyrst/Desktop/AA_Final/TheMatrix")
from matrix_implementations import *

def get_input_range(n):
    lower_bound = 0
    upper_bound = round(np.sqrt(2**(25)/n))
    input_range = [lower_bound, upper_bound]
    return input_range


def generate_input(n: int) -> List[float] :
    list= []
    input_range = get_input_range(n)
    for i in range(0,n*n):
        random.seed(i+3)
        l = random.randint(input_range[0],int(input_range[1]))
        list.append(float(l))
    return np.array(list).reshape(n,n)

def generate_floatinput(n: int, step: float) -> List[float]:
    list = []
    input_range = get_input_range(n)
    for i in range(0,n*n):
        random.seed(i+3)
        l = random.randint(input_range[0],int(input_range[1]))
        list.append(float(l)+step)
    return np.array(list).reshape(n,n)

n1 = 4
A1 = generate_floatinput(n1, 3.7497)
B1 = generate_floatinput(n1, 5.5208)

A11 = generate_input(n1)
B11 = generate_input(n1)

C1elementary = (elementary_multiplication(Matrix(n1,n1, A11), Matrix(n1,n1,B11))).tolist()
C1expected = np.matmul(A11,B11)

# print(np.testing.assert_allclose(C1elementary, C1expected, rtol=4.93169969e-07, atol=0))
print(np.testing.assert_array_equal(C1elementary,C1expected))


# n2 = 8
# A2 = generate_floatinput(n2, 2.0957)
# B2 = generate_floatinput(n2, 4.7604)

# A21 = generate_input(n2)
# B21 = generate_input(n2)

# n3 = 16
# A3 = generate_floatinput(n3, 7.0063)
# B3 = generate_floatinput(n3, 1.1111)

# A31 = generate_input(n3)
# B31 = generate_input(n3)

# n4 = 32
# A4 = generate_floatinput(n4, 0.0097)
# B4 = generate_floatinput(n4, 9.5678)

# A41 = generate_input(n4)
# B41 = generate_input(n4)

# n5 = 64
# A5 = generate_floatinput(n5, 1.7171)
# B5 = generate_floatinput(n5, 8.8675)

# A51 = generate_input(n5)
# B51 = generate_input(n5)

# C5tiled = tiled_multiplication(Matrix(n5,n5, A51),Matrix(n5,n5,B51),32).tolist()
# C5expected = np.matmul(A51, B51)

# print(np.testing.assert_allclose(C5tiled, C5expected))
# print(np.testing.assert_array_equal(C5tiled, C5expected))

# n6 = 128
# A6 = generate_floatinput(n6, 4.0903)
# B6 = generate_floatinput(n6, 0.0075)

# A61 = generate_input(n6)
# B61 = generate_input(n6)

# n7 = 256
# A7 = generate_floatinput(n7, 5.1903)
# B7 = generate_floatinput(n7, 1.1075)

# A71 = generate_input(n7)
# B71 = generate_input(n7)
