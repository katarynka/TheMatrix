import sys
import csv
from typing import List , Tuple , Optional , Dict , Callable , Any
import random

OptTuple3i = Optional[Tuple[int ,int ,int]]
FunType = Callable [[List[int]], OptTuple3i]


katarzyna = False
on_linux = True
sleep = True

if katarzyna:
    sys.path.append("/home/katarzyna/Documents/school/applied_algo/exam/fresh_copy/TheMatrix")
    path = "/home/katarzyna/Documents/school/applied_algo/exam/fresh_copy/TheMatrix/"
else:
    if on_linux == True:
        sys.path.append("/home/gustavgyrst/Desktop/AA_Final/TheMatrix")
        path = "/home/gustavgyrst/Desktop/AA_Final/TheMatrix/"
    else:
        sys.path.append("C:\\Users\\ggyrs\\OneDrive\\Desktop\\Matrix\\TheMatrix\\")
        path = "C:\\Users\\ggyrs\\OneDrive\\Desktop\\Matrix\\TheMatrix\\"
        
from matrix_implementations import *
from measurement import *


def write_csv(n_list: list, res: np.ndarray, filename: str, column_titles:list=None):
    """write_csv

    Args:
        n_list/m_list (list): list of n (the matrix side length) / m that the the experiment is run with
        res (np.ndarray): results from the experiment
        filename (str): the filename that you desire
        column_titles (lst): takes a list with the columns title for the csv file. The titles should be given comma seperated words and no spaces
    """
    with open(filename ,'w') as f:
        writer = csv.writer(f)
        if column_titles != None:
            writer.writerow(column_titles)
        for i in range(len(n_list)):
            writer.writerow ([n_list[i]] + res[i,:].tolist())

n = 32
m_list = [0,2,4,8,16]
N = 3 

def benchmark_recursive(f: FunType , m_list: list, n:int, N: int)->np.ndarray: 
    
    m_list_length = len(m_list)
    
    M: np.ndarray = np.zeros((m_list_length, N))
    # This loop takes each n in the n_list and puts in the randomly generated list
    for m in range(m_list_length):
        
        A = generate_input(n)
        B = generate_input(n)
        C = Matrix(n,n)
        
        if sleep: time.sleep(20)
        
        for j in range(N):
            M[m,j] = measure(lambda: f(A,B,C,m))
            print("time:")
            print(M[m,j])
            
            if sleep: time.sleep(5)
            
    means = np.mean(M,axis =1).reshape(m_list_length,1)
    stdevs = np.std(M,axis=1,ddof =1).reshape(m_list_length,1)
    return np.hstack ([means , stdevs ])

def benchmark_strassen(f: FunType , m_list: list, n:int, N: int)->np.ndarray:

    m_list_length = len(m_list)

    M: np.ndarray = np.zeros((m_list_length, N))
    # This loop takes each n in the n_list and puts in the randomly generated list
    for m in range(m_list_length):
        
        A = generate_input(n)
        B = generate_input(n)
        
        if sleep: time.sleep(20)
        
        for j in range(N):
            M[m,j] = measure(lambda: f(A,B,m))
            print("time:")
            print(M[m,j])
            
            if sleep: time.sleep(5)
            
    means = np.mean(M,axis =1).reshape(m_list_length,1)
    stdevs = np.std(M,axis=1,ddof =1).reshape(m_list_length,1)
    return np.hstack ([means , stdevs ])

# M-EXPERIMENT FOR WRITE-THROUGH
res_write_through = benchmark_recursive(recursive_multiplication_write_through, m_list, n, N)
title_write_through = "n" + str(n) + "_recursive_write_through_n_fixed_mtest.csv"
relative_path_write_through = "experiments/Results/write_through_m_experiments/"
full_path_write_through = path + relative_path_write_through + title_write_through
write_csv(m_list, res_write_through, full_path_write_through, ["n","time(s)","stdv"])


# M-EXPERIMENT FOR STRASSEN
res_strassen = benchmark_strassen(strassen, m_list, n, N)
title_strassen = "n" + str(n) + "_strassen_n_fixed_mtest.csv"
relative_path_strassen = "experiments/Results/strassen_m_experiments/"
full_path_strassen = path + relative_path_strassen + title_strassen
write_csv(m_list, res_strassen, full_path_strassen, ["n","time(s)","stdv"])

