import matplotlib.pyplot as plt # type: ignore
import csv
from typing import List , Tuple , Optional , Dict , Callable , Any
import numpy as np
from numpy.core.numeric import argwhere
from measurement import measure
import random
import sys
sys.path.append("/home/katarzyna/Documents/school/applied_algo/exam/TheMatrix")
from matrix_implementations import *

OptTuple3i = Optional[Tuple[int ,int ,int]]
FunType = Callable [[List[int]], OptTuple3i]


def benchmark(f: FunType , args: List[List[int]], N: int)->np.ndarray:
    m: int = len(args)
    M: np.ndarray = np.zeros ((m,N)) # measurements
    for i in range(len(args )):
        for j in range(N):
            temp = [list(l) for l in args]
            arg = list(temp[i])
            M[i,j] = measure(lambda: f(arg, 0, len(arg)-1))
    means = np.mean(M,axis =1).reshape(m,1)
    stdevs = np.std(M,axis=1,ddof =1).reshape(m,1)
    return np.hstack ([means , stdevs ])

    # benchmark(dual_pivot_quicksort, args1 , N)