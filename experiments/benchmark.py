# import matplotlib.pyplot as plt # type: ignore
import csv
from typing import List , Tuple , Optional , Dict , Callable , Any
import numpy as np
from numpy.core.numeric import argwhere
from measurement import *
import random
import sys
#sys.path.append("/home/katarzyna/Documents/school/applied_algo/exam/TheMatrix")
sys.path.append("/home/gustavgyrst/Desktop/AA_Final/TheMatrix")

from matrix_implementations import *

OptTuple3i = Optional[Tuple[int ,int ,int]]
FunType = Callable [[List[int]], OptTuple3i]

def benchmark(f: FunType , args1: List[Matrix], args2: List[Matrix], args3: List[Matrix], N: int)->np.ndarray:
    m: int = len(args1)
    M: np.ndarray = np.zeros ((m,N)) # measurements
    for i in range(len(args1)):
        for j in range(N):
            A = args1[i]
            B = args2[i]
            C = args3[i]
            M[i,j] = measure(lambda: f(A,B,C))
    means = np.mean(M,axis =1).reshape(m,1)
    stdevs = np.std(M,axis=1,ddof =1).reshape(m,1)
    return np.hstack ([means , stdevs ])

def rec_matmul_write_through(A: Matrix, B: Matrix, C: Matrix) -> Matrix:
    
    n = A.rows()    
    
    if n == 1:
        C[0] += A[0]*B[0]
        return C
    
    else:
        #M0 C upper left                        a00             b00             c00
        a00b00 = rec_matmul_write_through(A[:n//2,:n//2], B[:n//2,:n//2], C[:n//2,:n//2])
        #M1 C upper left                        a01             b10             c00
        a01b10 = rec_matmul_write_through(A[:n//2,n//2:], B[n//2:,:n//2], C[:n//2,:n//2])
        
        #M2 C upper right                       a00             b01             c01
        a00b01 = rec_matmul_write_through(A[:n//2,:n//2], B[:n//2,n//2:], C[:n//2,n//2:])
        #M3 C upper right                       a01             b11             c01
        a01b11 = rec_matmul_write_through(A[:n//2,n//2:], B[n//2:,n//2:], C[:n//2,n//2:])
        
        #M4 C lower left                        a10             b00             c10
        a10b00 = rec_matmul_write_through(A[n//2:,:n//2], B[:n//2,:n//2], C[n//2:,:n//2])
        #M5 C lower left                        a11             b10             c10
        a11b10 = rec_matmul_write_through(A[n//2:,n//2:], B[n//2:,:n//2], C[n//2:,:n//2])
        
        #M6 C lower right                       a10             b01             c11
        a10b01 = rec_matmul_write_through(A[n//2:,:n//2], B[:n//2,n//2:], C[n//2:,n//2:])
        #M7 C lower right                       a11             b11             c11
        a11b11 = rec_matmul_write_through(A[n//2:,n//2:], B[n//2:,n//2:], C[n//2:,n//2:])

        return C
    

N = 5
ns: List[int]
res_classic1: np.ndarray
res_dual1: np.ndarray
max_i: int = 11
N: int = 10
ns = [int (30*1.41**i) for i in range(max_i )]
n = 2

for i in range(6):
    print(n)
    args1 = [Matrix(n,n, np.array(generate_input(n)).reshape(n,n))for l in range(5)]
    args2 = [Matrix(n,n, np.array(generate_input(n)).reshape(n,n))for l in range(5)]
    args3 = [Matrix(n,n) for l in range(5)]

    res_elementary = benchmark(rec_matmul_write_through, args1 , args2, args3, N)
    print(res_elementary)
    n = n*2