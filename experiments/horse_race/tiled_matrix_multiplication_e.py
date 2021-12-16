from typing import List , Tuple , Optional ,  Callable 
import csv
import sys
import numpy as np

katarzyna = False
on_linux = True

if katarzyna:
    sys.path.append("/home/katarzyna/Documents/school/applied_algo/exam/fresh_copy/TheMatrix/experiments")
    path = "/home/katarzyna/Documents/school/applied_algo/exam/fresh_copy/TheMatrix/experiments/"
else:
    if on_linux == True:
        sys.path.append("/home/gustavgyrst/Desktop/AA_Final/TheMatrix/experiments/")
        path = "/home/gustavgyrst/Desktop/AA_Final/TheMatrix/experiments/"
    else:
        sys.path.append("C:\\Users\\ggyrs\\OneDrive\\Desktop\\Matrix\\TheMatrix\\experiments\\")
        path = "C:\\Users\\ggyrs\\OneDrive\\Desktop\\Matrix\\TheMatrix\\experiments\\"

from measurement import *
from horse_race_params import *

OptTuple3i = Optional[Tuple[int ,int ,int]]
FunType = Callable [[List[int]], OptTuple3i]

def benchmark_tiled(f: FunType , n_list: list, s:int, N: int)->np.ndarray: #N is repetitions
    
    n_list_length = len(n_list)
    
    M: np.ndarray = np.zeros((n_list_length, N))
    # This loop takes each n in the n_list and puts in the randomly generated list
    for n in range(n_list_length):     
        A = generate_input(n_list[n])
        B = generate_input(n_list[n])
            
        if warm_up == True:
            print("warm_up")
            f(A,B,s)
            f(A,B,s)
        
        print("show_time!")
        
        # Calculating the Dynamic S value so that it divides the matrix into 8 pieces (optimal).
        if (n>8):
            s = n/8
        else:
            s = n/2
            
        for j in range(N):
            M[n,j] = measure(lambda: f(A,B,s))
            print("time:")
            print(M[n,j])
            if sleep: time.sleep(5)
        if sleep: time.sleep(20)
    means = np.mean(M,axis =1).reshape(n_list_length,1)
    stdevs = np.std(M,axis=1,ddof =1).reshape(n_list_length,1)
    return np.hstack ([means , stdevs ])


def run_tiled_benchmark():
    print('tiled')
    res_tiled = benchmark_tiled(tiled_multiplication, n_list, s=s, N=N)
    tiled = path + relative_path + "tiled_multiplication_race.csv"
    write_csv(n_list, res_tiled, tiled, column_titles=column_titles)