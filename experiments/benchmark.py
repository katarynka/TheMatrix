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


ns: List[int]
N: int = 1
ns = [2,4,8,16,32,64,128,256,512,1024]




# tiled_N = 1024
# s_list = [2,4,8,16,32,64,128,256,512]
# args1 = [Matrix(tiled_N,tiled_N, np.array(generate_input(tiled_N)).reshape(tiled_N,tiled_N)) for s in s_list]
# args2 = [Matrix(tiled_N,tiled_N, np.array(generate_input(tiled_N)).reshape(tiled_N,tiled_N)) for s in s_list]

# res_tiled = benchmark_tiled(tiled_multiplication, args1 , args2, s_list, N)
# print(res_tiled)


def write_csv(ns: List[int], res: np.ndarray ,
            filename: str):
    with open(filename ,'w') as f:
        writer = csv.writer(f)
        for i in range(len(ns)):
            writer.writerow ([ns[i]] + res[i,:]. tolist ())

def write_csv_tiled(ns: List[int], res: np.ndarray ,
            filename: str):
    with open(filename ,'w') as f:
        writer = csv.writer(f)
        for i in range(len(s_list)):
            writer.writerow ([s_list[i]] + res[i,:]. tolist ())

#write_csv_tiled(ns, res_tiled, "tiled.csv")

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