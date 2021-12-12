import sys
sys.path.append("/home/gustavgyrst/Desktop/AA_Final/TheMatrix/")
#sys.setrecursionlimit(2000) Probably not necessary
from matrix_implementations import *
import random
import numpy as np


def get_input_range(n):
    lower_bound = 0
    upper_bound = round(np.sqrt(float(2**(53))/n))
    input_range = [lower_bound, upper_bound]
    return input_range


def generate_input(n: int) -> Matrix :
    list= []
    input_range = get_input_range(n)
    for i in range(0,n*n):
        l = random.randint(input_range[0],int(input_range[1]))
        list.append(float(l))
    return np.array(list).reshape(n,n)

n=64

A = generate_input(n)
B = generate_input(n)

Am = Matrix(n,n,np.array(A).reshape(n,n))
Bm = Matrix(n,n,np.array(B).reshape(n,n))
            
#strass = strassen(Am, Bm)
rec = recursive_multiplication_write_through(Am,Bm, Matrix(Am.rows(), Am.rows()))

res = np.matmul(A,B) 

#np.testing.assert_equal(strass, res)
np.testing.assert_equal(rec, res)
