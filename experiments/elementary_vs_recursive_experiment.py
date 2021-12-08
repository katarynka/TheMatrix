import sys
#sys.path.append("/home/katarzyna/Documents/school/applied_algo/exam/TheMatrix")
sys.path.append("/home/gustavgyrst/Desktop/AA_Final/TheMatrix")

from matrix_implementations import *
from benchmark import *
from measurement import *



args1 = [generate_input(n) for n in ns]
args2 = [generate_input(n) for n in ns]
args3 = [Matrix(n,n) for n in ns]

res_elementary = benchmark_elementary(elementary_multiplication, args1 , args2, N)
print(res_elementary)


# args1 = [Matrix(n,n, np.array(generate_input(n)).reshape(n,n))for n in ns]
# args2 = [Matrix(n,n, np.array(generate_input(n)).reshape(n,n))for n in ns]
# args3 = [Matrix(n,n) for n in ns]

# res_recursive_write_through = benchmark_ABC_matrices(rec_matmul_write_through, args1 , args2, args3, N)
# print(res_recursive_write_through)


write_csv(ns, res_elementary, "elementary_full.csv")
#write_csv(ns, res_recursive_write_through, "recursive_write_through.csv")

