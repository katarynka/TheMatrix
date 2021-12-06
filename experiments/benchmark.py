# import matplotlib.pyplot as plt 
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

def benchmark_ABC_matrices(f: FunType , args1: List[Matrix], args2: List[Matrix], args3: List[Matrix], N: int)->np.ndarray:
    m: int = len(args1)
    M: np.ndarray = np.zeros ((m,N)) # measurements
    for i in range(len(args1)):
        for j in range(N):
            A = args1[i]
            B = args2[i]
            C = args3[i]
            print("recursive rows")
            print(A.rows())
            M[i,j] = measure(lambda: f(A,B,C))
    means = np.mean(M,axis =1).reshape(m,1)
    stdevs = np.std(M,axis=1,ddof =1).reshape(m,1)
    return np.hstack ([means , stdevs ])

def benchmark_elementary(f: FunType , args1: List[Matrix], args2: List[Matrix], N: int)->np.ndarray:
    m: int = len(args1)
    M: np.ndarray = np.zeros ((m,N)) # measurements
    for i in range(len(args1)):
        for j in range(N):
            A = args1[i]
            B = args2[i]
            print("elementary rows") 
            print(A.rows())
            M[i,j] = measure(lambda: f(A,B))
    means = np.mean(M,axis =1).reshape(m,1)
    stdevs = np.std(M,axis=1,ddof =1).reshape(m,1)
    return np.hstack ([means , stdevs ])

def benchmark_tiled(f: FunType , args1: List[Matrix], args2: List[Matrix], args3: List[int], N: int)->np.ndarray:
    m: int = len(args1)
    M: np.ndarray = np.zeros ((m,N)) # measurements
    for i in range(len(args1)):
        for j in range(N):
            A = args1[i]
            B = args2[i]
            s = args3[i]
            print("tiled rows") 
            print(A.rows())
            M[i,j] = measure(lambda: f(A,B,s))
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
    


ns: List[int]
N: int = 10
ns = [2,4,8,16,32,64,128,256,512]


args1 = [Matrix(n,n, np.array(generate_input(n)).reshape(n,n))for n in ns]
args2 = [Matrix(n,n, np.array(generate_input(n)).reshape(n,n))for n in ns]
args3 = [Matrix(n,n) for n in ns]

res_elementary = benchmark_elementary(elementary_multiplication, args1 , args2, N)
print(res_elementary)


args1 = [Matrix(n,n, np.array(generate_input(n)).reshape(n,n))for n in ns]
args2 = [Matrix(n,n, np.array(generate_input(n)).reshape(n,n))for n in ns]
args3 = [Matrix(n,n) for n in ns]

res_recursive_write_through = benchmark_ABC_matrices(rec_matmul_write_through, args1 , args2, args3, N)
print(res_recursive_write_through)

tiled_N = 1024
args3 = [2,4,8,16,32,64,128,256,512]
args1 = [Matrix(tiled_N,tiled_N, np.array(generate_input(tiled_N)).reshape(tiled_N,tiled_N)) for n in args3]
args2 = [Matrix(tiled_N,tiled_N, np.array(generate_input(tiled_N)).reshape(tiled_N,tiled_N)) for n in args3]

res_tiled = benchmark_tiled(tiled_multiplication, args1 , args2, args3, N)
print(res_tiled)


def write_csv(ns: List[int], res: np.ndarray ,
            filename: str):
    with open(filename ,'w') as f:
        writer = csv.writer(f)
        for i in range(len(ns)):
            writer.writerow ([ns[i]] + res[i,:]. tolist ())

write_csv(ns, res_elementary, "elementary.csv")
write_csv(ns, res_recursive_write_through, "recursive_write_through.csv")


# fig = plt.figure ()
# ax = fig.gca()
# ax.errorbar(ns, res_elementary [:,0], res_elementary [:,1],
# capsize = 3.0, marker = 'o')
# ax.errorbar(ns, res_recursive_write_through [:,0], res_recursive_write_through [:,1],
# capsize = 3.0, marker = 'o')
# ax.set_xlabel('Value of n')
# ax.set_ylabel('Time (s)')
# ax.set_yscale('log')
# ax.legend (['Elementary multiplication ', 'Recursive write through multiplication '])
# plt.savefig('elementary_vs_write_through.pdf')