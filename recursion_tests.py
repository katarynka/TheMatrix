import matrix_implementations as m
import numpy as np


test = np.array([[1,1,1,1],
                 [2,2,2,2],
                 [3,3,3,3],
                 [4,4,4,4]])

test2 = np.array([[1,1,1,1],
                 [2,2,2,2],
                 [3,3,3,3],
                 [4,4,4,4]])

m.recursive_multiplication_write_through(test, test2, 3)