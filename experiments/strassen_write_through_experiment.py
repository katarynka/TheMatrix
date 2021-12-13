import sys
import csv
from typing import List , Tuple , Optional , Dict , Callable , Any
import random

katarzyna = True

if katarzyna:
    sys.path.append("/home/katarzyna/Documents/school/applied_algo/exam/fresh_copy/TheMatrix")
    path = "/home/katarzyna/Documents/school/applied_algo/exam/fresh_copy/TheMatrix/"
else:
    sys.path.append("/home/gustavgyrst/Desktop/AA_Final/TheMatrix")
    path = "/home/gustavgyrst/Desktop/AA_Final/TheMatrix/"

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
        random.seed(n + i)
        l = random.randint(input_range[0],int(input_range[1]))
        list.append(float(l))
    return Matrix(n,n,np.array(list).reshape(n,n))


def benchmark_recursive(f: FunType , n_list: list, m: int, N: int)->np.ndarray: #N is repetitions
    
    n_list_length = len(n_list)
    
    M: np.ndarray = np.zeros((n_list_length, N))
    # This loop takes each n in the n_list and puts in the randomly generated list
    for n in range(n_list_length):
        
        A = generate_input(n_list[n])
        B = generate_input(n_list[n])
        C = Matrix(n_list[n],n_list[n])
    
        for j in range(N):
            M[n,j] = measure(lambda: f(A,B,C,m))
            print("time:")
            print(M[n,j])
            # time.sleep(20)
    means = np.mean(M,axis =1).reshape(n_list_length,1)
    stdevs = np.std(M,axis=1,ddof =1).reshape(n_list_length,1)
    return np.hstack ([means , stdevs ])

def benchmark_strassen(f: FunType , n_list: list, m: int, N: int)->np.ndarray: #N is repetitions

    n_list_length = len(n_list)

    M: np.ndarray = np.zeros((n_list_length, N))
    # This loop takes each n in the n_list and puts in the randomly generated list
    for n in range(n_list_length):
        
        A = generate_input(n_list[n])
        B = generate_input(n_list[n])

        for j in range(N):
            M[n,j] = measure(lambda: f(A,B,m))
            print("time:")
            print(M[n,j])
            # time.sleep(20)
    means = np.mean(M,axis =1).reshape(n_list_length,1)
    stdevs = np.std(M,axis=1,ddof =1).reshape(n_list_length,1)
    return np.hstack ([means , stdevs ])


def write_csv(n_list: list, res: np.ndarray, filename: str, column_titles:str=None):
    """write_csv

    Args:
        n_list (list): list of n (the matrix side length) that the the experiment is run with
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

# The number of repetition we have for each experiment we run
N = 3
# list of n-values we test on.
n_list = [8,16,32,64]
# The list of m we are testing.
m_list = [0,2,4,8,16,32]

# for m in m_list:
#     res = benchmark_recursive(recursive_multiplication_write_through, n_list, m, N)
#     relative_path = "experiments/Results/write_through_m_experiments/"
#     title = path + relative_path + str(m) + "_recursive_write_through_matrix_multiplication_mtest.csv"
    
#     write_csv(n_list, res, title, column_titles=["n","time","stdv"])


for m in m_list:
    res = benchmark_strassen(strassen, n_list, m, N)
    relative_path = "experiments/Results/strassen_m_experiments/"
    title = path + relative_path + str(m) + "strassen_matrix_multiplication_mtest.csv"
    write_csv(n_list, res, title, column_titles=["n","time","stdv"])
