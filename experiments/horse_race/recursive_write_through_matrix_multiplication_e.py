from typing import List , Tuple , Optional ,  Callable 
import csv
import sys
import numpy as np

on_linux = True
from horse_race_params import *


if katarzyna:
    sys.path.append("/home/katarzyna/Documents/school/applied_algo/exam/fresh_copy/TheMatrix/experiments")
    path = "/home/katarzyna/Documents/school/applied_algo/exam/fresh_copy/TheMatrix/experiments/"
else:
    if on_linux == True:
        sys.path.append("/home/gustavgyrst/Desktop/AA_Final/TheMatrix/experiments/")
        path = "/home/gustavgyrst/Desktop/AA_Final/TheMatrix/experiments/"
    else:
        sys.path.append("C:\\Users\\ggyrs\\OneDrive\\Desktop\\Matrix\\TheMatrix\\experiments\\")
        path = "C:\\Users\\ggyrs\\OneDrive\\Desktop\\Matrix\\TheMatrix\\experiments"

from measurement import *

OptTuple3i = Optional[Tuple[int ,int ,int]]
FunType = Callable [[List[int]], OptTuple3i]

def benchmark_write_through(f: FunType , n_list: list, m:int, N: int)->np.ndarray: #N is repetitions
    
    n_list_length = len(n_list)
    
    M: np.ndarray = np.zeros((n_list_length, N))
    # This loop takes each n in the n_list and puts in the randomly generated list
    for n in range(n_list_length):     
        A = generate_input(n_list[n])
        B = generate_input(n_list[n])
        
        if warm_up == True:
            print("warm_up")
            C = Matrix(n_list[n],n_list[n])
            f(A,B,C,m)
            C = Matrix(n_list[n],n_list[n])
            f(A,B,C,m)
        
        print("Show-time!")    
        for j in range(N):
            C = Matrix(n_list[n],n_list[n])
            M[n,j] = measure(lambda: f(A,B,C,m))
            print("time:")
            print(M[n,j])
            if sleep: time.sleep(5)
        if sleep: time.sleep(20)
    means = np.mean(M,axis =1).reshape(n_list_length,1)
    stdevs = np.std(M,axis=1,ddof =1).reshape(n_list_length,1)
    return np.hstack ([means , stdevs ])




def run_write_through_benchmark():
    print("write_through")
    res_write_through = benchmark_write_through(recursive_multiplication_write_through, n_list, m=m_write_trhough, N=N)
    write_through = path + relative_path + file_name + "recursive_write_through_multiplication_race.csv"
    write_csv(n_list, res_write_through, write_through, column_titles=column_titles)