import sys
import csv
from typing import List , Tuple , Optional , Dict , Callable , Any
import random

OptTuple3i = Optional[Tuple[int ,int ,int]]
FunType = Callable [[List[int]], OptTuple3i]


katarzyna = False
on_linux = True

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

#3! different permutations / orders --> Therefore we have the following combinations:

ijk_order = [['i','j','k'], 
         ['i','k','j'], 
         ['k','i','j'], 
         ['k','j','i'], 
         ['j','k','i'], 
         ['j','i','k']]

def elementary_multiplication_ijk(A: Matrix, B: Matrix, order:list)->Matrix:
    n = A.cols()
    C = Matrix(n,n)
    
    for order[0] in range(n):
        for order[1] in range(n):
            for order[2] in range(n):
                C._arr[order[0],order[1]] += A._arr[order[0],[order[2]]]*B._arr[order[2],order[1]]
    return C


# If you want to run a quick test.
quick_test = False
if quick_test == True:
    M1 = Matrix(4,4, np.array([-5, 8, -7, -10, -1, -1, 3, -5, -2, -9, 5, -10, 6, -2, 2, -10], dtype=float).reshape(4,4))
    M2 = Matrix(4,4, np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],dtype=float).reshape(4,4))
    C = Matrix(M1.rows(), M1.rows())

    M11 = np.array([-5, 8, -7, -10, -1, -1, 3, -5, -2, -9, 5, -10, 6, -2, 2, -10]).reshape(4,4)
    M21 = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]).reshape(4,4)


    print(elementary_multiplication_ijk(M1,M2, order[5]))
    print(np.matmul(M11,M21))

N = 1
n_list = [2,4,8,16,32,64,128]

def benchmark_elementary_ijk(f: FunType , n_list: list, order:list, N: int)-> np.ndarray:
    
    n_list_length = len(n_list)
    
    M: np.ndarray = np.zeros((n_list_length, N))
        
    # This loop takes each n in the n_list and puts in the randomly generated list    
    for n in range(n_list_length):
    
        A = generate_input(n_list[n])
        B = generate_input(n_list[n])
        #time.sleep(20)
    
        for j in range(N):
            M[n,j] = measure(lambda: f(A,B, order))
            print("time:")
            print(M[n,j])
            #time.sleep(5)
    means = np.mean(M,axis =1).reshape(n_list_length,1)
    stdevs = np.std(M,axis=1,ddof =1).reshape(n_list_length,1)
    return np.hstack([means , stdevs])


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



 # This loop goes through all the ijk_order combinations
for ijk in ijk_order:
    ijk_order_name = ijk[0] + ijk[1] + ijk[2]
    res = benchmark_elementary_ijk(elementary_multiplication_ijk, n_list, ijk, N)
    
    relative_path = "experiments/Results/elementary_ijk_experiment/"
    title = path + relative_path + ijk_order_name + "_elementary_ijk_experiment_order.csv"
    write_csv(n_list, res, title, column_titles=["n","time(s)","stdv"])

