from typing import Callable , Any
import time
import numpy as np
from typing import List
import random
import sys
sys.path.append("/home/katarzyna/Documents/school/applied_algo/exam/TheMatrix")
from matrix_implementations import *

def measure(f: Callable [[],Any])->float:
    start: float = time.time()
    f()
    end: float = time.time()
    return end - start


def generate_input(n: int) -> List[int] :
    list= []
    for i in range(0,n*n):
        random.seed(i+3)
        l = random.randint(1,3000)
        list.append(l)
    return list

N = 128

l1 = generate_input(N)
l2 = generate_input(N)
A = Matrix(N,N,np.array(l1).reshape(N,N))
B = Matrix(N,N,np.array(l2).reshape(N,N))
t5 = measure(lambda: tiled_multiplication(A,B,16))

print(t5)