from typing import List , Tuple , Optional ,  Callable 
import csv
import sys
import numpy as np

katarzyna = True

if katarzyna:
    sys.path.append("/home/katarzyna/Documents/school/applied_algo/exam/fresh_copy/TheMatrix/experiments")
else:
    sys.path.append("/home/gustavgyrst/Desktop/AA_Final/TheMatrix")

from measurement import *

OptTuple3i = Optional[Tuple[int ,int ,int]]
FunType = Callable [[List[int]], OptTuple3i]


def benchmark(f: FunType , n_list: list, N: int, int_param: int=None, in_place:bool=False)->np.ndarray: #N is repetitions
    
    n_list_length = len(n_list)
    
    M: np.ndarray = np.zeros((n_list_length, N))
    # This loop takes each n in the n_list and puts in the randomly generated list
    for n in range(n_list_length):
        
        A = generate_input(n_list[n])
        B = generate_input(n_list[n]) # traspose for transposed!!!!
        # time.sleep(20) 
        if(in_place):
            C = Matrix(n_list[n],n_list[n])
        for j in range(N):
            if in_place:
                print("here should be write_through")
                print(str(f))
                print(f(A,B, C,int_param))
                M[n,j] = measure(lambda: f(A,B,C,int_param))
            else:
                if int_param == None:
                    M[n,j] = measure(lambda: f(A,B))
                    print(str(f))
                    print(f(A,B))
                    # print("time:")
                    # print(M[n,j])
                    # time.sleep(5)
                else:
                    print("here should be strassen and tiled")
                    print(str(f))
                    M[n,j] = measure(lambda: f(A,B,int_param))
                    print(f(A,B,int_param))
                    # print("time:")
                    # print(M[n,j])
                    # time.sleep(5)
                    # print("time:")
                    # print(M[n,j])
                    # time.sleep(5)
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