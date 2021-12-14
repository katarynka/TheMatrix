from typing import List , Tuple , Optional , Dict , Callable , Any
import time
import numpy as np
import random
import sys
import random

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

def measure(f: Callable [[],Any])->float:
    start: float = time.time()
    f()
    end: float = time.time()
    return end - start


def get_input_range(n):
    lower_bound = 0
    upper_bound = round(np.sqrt(2**(53)/n))
    input_range = [lower_bound, upper_bound]
    return input_range


def generate_input(n: int) -> Matrix :
    list= []
    input_range = get_input_range(n)
    for i in range(0,n*n):
        random.seed(i+n)
        l = random.randint(input_range[0],int(input_range[1]))
        list.append(float(l))
    return Matrix(n,n,np.array(list).reshape(n,n))
