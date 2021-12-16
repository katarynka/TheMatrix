import sys
import csv
from typing import List , Tuple , Optional , Dict , Callable , Any


katarzyna = False
on_linux = True
sleep = False
warmup = True

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

OptTuple3i = Optional[Tuple[int ,int ,int]]
FunType = Callable [[List[int]], OptTuple3i]

def benchmark_tiled(f: FunType , s_list: list, n:int, N: int)->np.ndarray:

    s_list_length = len(s_list)

    M: np.ndarray = np.zeros((s_list_length, N))
    # This loop takes each n in the n_list and puts in the randomly generated list
    for s in range(s_list_length):
        
        A = generate_input(n)
        B = generate_input(n)
        
        if sleep: time.sleep(20)
        
        if warmup:
            f(A,B,s_list[s])
            f(A,B,s_list[s])

        for j in range(N):
            M[s,j] = measure(lambda: f(A,B,s_list[s]))
            print("time:")
            print(M[s,j])
            
            if sleep: time.sleep(5)
            
    means = np.mean(M,axis =1).reshape(s_list_length,1)
    stdevs = np.std(M,axis=1,ddof =1).reshape(s_list_length,1)
    return np.hstack ([means , stdevs ])


N = 3
tiled_N = 128
s_list = [2,4,8,16,32,64]



res_tiled = benchmark_tiled(tiled_multiplication, s_list, tiled_N, N)
print(res_tiled)


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

relative_path = "experiments/tiled_experiment/"
tiled = path + relative_path + "128n_tiled_multiplication_s_experiment.csv"
column_titles = ["s","time","stdv"]
write_csv(s_list, res_tiled, tiled, column_titles)
