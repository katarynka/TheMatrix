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

N = 256
s = 128
print("N ") 
print(N)
print("s ")
print(s)
l1 = generate_input(N)
l2 = generate_input(N)
A = Matrix(N,N,np.array(l1).reshape(N,N))
B = Matrix(N,N,np.array(l2).reshape(N,N))
C = Matrix(N,N,np.array(generate_input(N)).reshape(N,N))
D = Matrix(N,N,np.array(generate_input(N)).reshape(N,N))
t5 = measure(lambda: tiled_multiplication(A,B,s))
t6 = measure(lambda: tiled_multiplication2(C,D,s))

print("without function call")
print(t6)
print("with function call")
print(t5)