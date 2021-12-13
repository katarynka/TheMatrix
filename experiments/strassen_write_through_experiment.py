import sys
import csv
from typing import List , Tuple , Optional , Dict , Callable , Any
import random
#sys.path.append("/home/katarzyna/Documents/school/applied_algo/exam/TheMatrix")
sys.path.append("/home/gustavgyrst/Desktop/AA_Final/TheMatrix")

from matrix_implementations import *
from measurement import *

OptTuple3i = Optional[Tuple[int ,int ,int]]
FunType = Callable [[List[int]], OptTuple3i]

def get_input_range(n):
    lower_bound = 0
    upper_bound = round(np.sqrt(2**(53)/n))
    input_range = [lower_bound, upper_bound]
    return input_range


def generate_input(n: int) -> Matrix :
    list= []
    input_range = get_input_range(n)
    for i in range(0,n*n):
        random.seed(n)
        l = random.randint(input_range[0],int(input_range[1]))
        list.append(float(l))
    return Matrix(n,n,np.array(list).reshape(n,n))


def benchmark_recursive(f: FunType , args1: List[Matrix], args2: List[Matrix], args3: List[Matrix], em: int, N: int)->np.ndarray:
    m: int = len(args1)
    M: np.ndarray = np.zeros ((m,N)) # measurements
    for i in range(len(args1)):
        for j in range(N):
            A = args1[i]
            B = args2[i]
            C = args3[i]
            print("m") 
            print(em)
            M[i,j] = measure(lambda: f(A,B,C,em))
            print("time:")
            print(M[i,j])
            # time.sleep(20)
    means = np.mean(M,axis =1).reshape(m,1)
    stdevs = np.std(M,axis=1,ddof =1).reshape(m,1)
    return np.hstack ([means , stdevs ])

def benchmark_strassen(f: FunType , args1: List[Matrix], args2: List[Matrix], args3: List[int], N: int)->np.ndarray:
    m: int = len(args3)
    M: np.ndarray = np.zeros ((m,N)) # measurements
    for i in range(len(args3)):
        for j in range(N):
            A = args1[i]
            B = args2[i]
            em = args3[i]
            print("m") 
            print(em)
            M[i,j] = measure(lambda: f(A,B,em))
            print("time:")
            print(M[i,j])
            # time.sleep(20)
    means = np.mean(M,axis =1).reshape(m,1)
    stdevs = np.std(M,axis=1,ddof =1).reshape(m,1)
    return np.hstack ([means , stdevs ])

N = 3
m_list = [0,2,4,8,16,32,64,128]
# args1 = [generate_input(n) for n in ns]
# args2 = [generate_input(n) for n in ns]
# args3 = [Matrix(n,n) for n in ns]
ns = [8,16,32,64,128,256]

res_write_through = []
for m in m_list:
    n_list = []
    args1 = [generate_input(n) for n in n_list]
    args2 = [generate_input(n) for n in n_list]
    args3 = [Matrix(n,n) for n in ns]
    res = benchmark_recursive(recursive_multiplication_write_through, args1, args2, args3, m, N)
    res_write_through.append(res)


# res_write_through = benchmark_recursive(recursive_multiplication_write_through, args1 , args2, args3, m_list, N)


# time.sleep(300)
# print("Continues for test with Strassen")


# res_strassen = benchmark_strassen(strassen, args1 , args2, m_list, N)
# print(res_write_through)

# print(res_strassen)

# def write_csv_tiled(ns: List[int], res: np.ndarray, filename: str):
#     with open(filename ,'w') as f:
#         writer = csv.writer(f)
#         for i in range(len(m_list)):
#             writer.writerow ([m_list[i]] + res[i,:]. tolist ())

# write_csv_tiled(m_list, res_write_through, "write_throughM2.csv")
# write_csv_tiled(m_list, res_strassen, "strassenKTOB.csv")
