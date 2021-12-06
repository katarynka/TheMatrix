from typing import Callable , Any
import time
import numpy as np
from typing import List
import random
import sys
#sys.path.append("/home/katarzyna/Documents/school/applied_algo/exam/TheMatrix")
sys.path.append("/home/gustavgyrst/Desktop/AA_Final/TheMatrix")
from matrix_implementations import *

def measure(f: Callable [[],Any])->float:
    start: float = time.time()
    f()
    end: float = time.time()
    return end - start


def get_input_range(n):
    lower_bound = 0
    upper_bound = round(np.sqrt(2**(53)/n))
    input_range = [lower_bound, upper_bound]
    return input_range

print(get_input_range(256))

def generate_input(n: int) -> List[int] :
    list= []
    input_range = get_input_range(n)
    for i in range(0,n*n):
        random.seed(i+3)
        l = random.randint(input_range[0],int(input_range[1]))
        list.append(l)
    return list

generate_input(256)
print()

# N = 256
# s = 128
# print("N ") 
# print(N)
# print("s ")
# print(s)
# l1 = generate_input(N)
# l2 = generate_input(N)
# A = Matrix(N,N,np.array(l1).reshape(N,N))
# B = Matrix(N,N,np.array(l2).reshape(N,N))
# C = Matrix(N,N,np.array(generate_input(N)).reshape(N,N))
# D = Matrix(N,N,np.array(generate_input(N)).reshape(N,N))
# t5 = measure(lambda: tiled_multiplication(A,B,s))
# t6 = measure(lambda: tiled_multiplication(C,D,s))
