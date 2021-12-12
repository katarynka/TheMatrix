import sys
import csv
from typing import List , Tuple , Optional , Dict , Callable , Any
sys.path.append("/home/katarzyna/Documents/school/applied_algo/exam/TheMatrix")
# sys.path.append("/home/gustavgyrst/Desktop/AA_Final/TheMatrix")

from matrix_implementations import *
from measurement import *

OptTuple3i = Optional[Tuple[int ,int ,int]]
FunType = Callable [[List[int]], OptTuple3i]

def benchmark_tiled(f: FunType , args1: List[Matrix], args2: List[Matrix], args3: List[int], N: int)->np.ndarray:
    m: int = len(args3)
    M: np.ndarray = np.zeros ((m,N)) # measurements
    for i in range(len(args3)):
        # tiled_multiplication(args1[i],args2[i],args3[i])
        for j in range(N):
            A = args1[i]
            B = args2[i]
            s = args3[i]
            print("tiled s") 
            print(s)
            M[i,j] = measure(lambda: f(A,B,s))
            print("time")
            print(M[i,j])
    means = np.mean(M,axis =1).reshape(m,1)
    stdevs = np.std(M,axis=1,ddof =1).reshape(m,1)
    return np.hstack ([means , stdevs ])

N = 3
tiled_N = 512
s_list = [2,4,8,16,32,64,128,256]

args1 = [generate_input(tiled_N) for s in s_list]
args2 = [generate_input(tiled_N) for s in s_list]


res_tiled = benchmark_tiled(tiled_multiplication_fun_call, args1 , args2, s_list, N)
print(res_tiled)


def write_csv_tiled(ns: List[int], res: np.ndarray ,
            filename: str):
    with open(filename ,'w') as f:
        writer = csv.writer(f)
        for i in range(len(s_list)):
            writer.writerow ([s_list[i]] + res[i,:]. tolist ())


write_csv_tiled(s_list, res_tiled, "tiledfunKTOB.csv")
