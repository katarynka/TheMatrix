import sys
#sys.path.append("/home/katarzyna/Documents/school/applied_algo/exam/TheMatrix")
sys.path.append("/home/gustavgyrst/Desktop/AA_Final/TheMatrix")
from matrix_implementations import *
from benchmark import *
from measurement import *

ns = [2,4,8,16,32,64,128,256]

def benchmark(f: FunType , args1: List[Matrix], args2: List[Matrix], args3: List[Matrix], N: int)->np.ndarray:
    m: int = len(args1)
    M: np.ndarray = np.zeros ((m,N)) # measurements
    for i in range(len(args1)):
        for j in range(N):
            A = args1[i]
            B = args2[i]
            C = args3[i]
            print("elementary rows") 
            print(A.rows())
            M[i,j] = measure(lambda: f(A,B,C))
    means = np.mean(M,axis =1).reshape(m,1)
    stdevs = np.std(M,axis=1,ddof =1).reshape(m,1)
    return np.hstack ([means , stdevs ])

args1 = [generate_input(n) for n in ns]
args2 = [generate_input(n) for n in ns]
args3 = [Matrix(n,n) for n in ns]

# res_elementary = benchmark_elementary(elementary_multiplication, args1 , args2, N)
res_elementary = benchmark(elementary_multiplication_in_place, args1 , args2, args3, N)
print(res_elementary)


# args1 = [Matrix(n,n, np.array(generate_input(n)).reshape(n,n))for n in ns]
# args2 = [Matrix(n,n, np.array(generate_input(n)).reshape(n,n))for n in ns]
# args3 = [Matrix(n,n) for n in ns]

# res_recursive_write_through = benchmark_ABC_matrices(rec_matmul_write_through, args1 , args2, args3, N)
# print(res_recursive_write_through)


write_csv(ns, res_elementary, "elementary_full_optimized.csv")
#write_csv(ns, res_recursive_write_through, "recursive_write_through.csv")

