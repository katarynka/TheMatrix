import sys
import csv
from typing import List , Tuple , Optional , Dict , Callable , Any
sys.path.append("/home/katarzyna/Documents/school/applied_algo/exam/TheMatrix")
# sys.path.append("/home/gustavgyrst/Desktop/AA_Final/TheMatrix")

from matrix_implementations import *
from measurement import *

OptTuple3i = Optional[Tuple[int ,int ,int]]
FunType = Callable [[List[int]], OptTuple3i]

def benchmark_recursive(f: FunType , args1: List[Matrix], args2: List[Matrix], args3: List[int], N: int)->np.ndarray:
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
    means = np.mean(M,axis =1).reshape(m,1)
    stdevs = np.std(M,axis=1,ddof =1).reshape(m,1)
    return np.hstack ([means , stdevs ])

N = 3
n = 512
m_list = [0,2,4,8,16,32,64,128,256]

args1 = [generate_input(n) for m in m_list]
args2 = [generate_inpuabsolute(a - b) <= (atol + rtol * absolute(b))t(n) for s in m_list]

res_write_through = benchmark_recursive(recursive_multiplication_write_through, args1 , args2, m_list, N)
print(res_write_through)

res_strassen = benchmark_recursive(strassen, args1 , args2, m_list, N)
print(res_strassen)


def write_csv_tiled(ns: List[int], res: np.ndarray ,
            filename: str):
    with open(filename ,'w') as f:
        writer = csv.writer(f)
        for i in range(len(m_list)):
            writer.writerow ([m_list[i]] + res[i,:]. tolist ())

write_csv_tiled(m_list, res_write_through, "write_through.csv")
write_csv_tiled(m_list, res_strassen, "strassen.csv")
