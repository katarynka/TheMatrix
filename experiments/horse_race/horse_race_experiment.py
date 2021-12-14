import time
from horse_race_benchmark import benchmark, write_csv
import numpy as np
import sys

katarzyna = True

if katarzyna:
    sys.path.append("/home/katarzyna/Documents/school/applied_algo/exam/fresh_copy/TheMatrix")
    path = "/home/katarzyna/Documents/school/applied_algo/exam/fresh_copy/TheMatrix/"
else:
    sys.path.append("/home/gustavgyrst/Desktop/AA_Final/TheMatrix")
    path = "/home/gustavgyrst/Desktop/AA_Final/TheMatrix/"

from matrix_implementations import *

relative_path = "experiments/horse_race/horse_race_results/"
column_titles = ["n","time","stdv"]

N = 1
n_list = [2,4]
s = 2
m = 2
def tiled_multiplication(A: Matrix, B: Matrix, s: int)->Matrix:                
    n = A.cols()
    C = Matrix(n,n)

    for i in range(n//s):
        for j in range(n//s):
            for k in range(n//s):
                subA = A[i*s:i*s+s,k*s:k*s+s]
                subB = B[k*s:k*s+s,j*s:j*s+s]
                z = subA.cols()
                subC = Matrix(z,z)
                for l in range(z):
                    for m in range(z):
                        for o in range(z):
                            temp = subC[l,m] + subA[l,o]*subB[o,m]
                            subC[l,m] = temp
                C[i*s:i*s+s,j*s:j*s+s].__iadd__(subC)

    return C

A = Matrix(4,4, np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]).reshape(4,4))    

res_elementary = benchmark(elementary_multiplication, n_list, N=N)

time.sleep(100)


res_transposed = benchmark(elementary_multiplication_transposed, n_list, N)

time.sleep(100)

res_copying = benchmark(recursive_multiplication_copying, n_list, N)

time.sleep(100)

res_tiled = benchmark(tiled_multiplication, n_list, N, s)

time.sleep(100)

res_strassen = benchmark(strassen, n_list, N, m)

time.sleep(100)

res_write_through = benchmark(recursive_multiplication_write_through, n_list, N, m, in_place=True)

elementary = path + relative_path + "elementary_multiplication_race.csv"
write_csv(n_list, res_elementary, elementary, column_titles=column_titles)

transposed = path + relative_path + "elementary_transposed_multiplication_race.csv"
write_csv(n_list, res_transposed, transposed, column_titles=column_titles)

tiled = path + relative_path + "tiled_multiplication_race.csv"
write_csv(n_list, res_tiled, tiled, column_titles=column_titles)

copying = path + relative_path + "recursive_copying_multiplication_race.csv"
write_csv(n_list, res_copying, copying, column_titles=column_titles)

strassens = path + relative_path + "strassen_multiplication_race.csv"
write_csv(n_list, res_strassen, strassens, column_titles=column_titles)

write_through = path + relative_path + "recursive_write_through_multiplication_race.csv"
write_csv(n_list, res_write_through, write_through, column_titles=column_titles)

