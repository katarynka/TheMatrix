import random
from typing import List
import sys
sys.path.append("/home/katarzyna/Documents/school/applied_algo/exam/TheMatrix")
from matrix_implementations import *

def generate_input(n: int) -> List[int] :
    list= []
    for i in range(0,n*n):
        random.seed(i+3)
        l = random.randint(1,3000)
        list.append(l)
    
    return Matrix(n,n,np.array(list).reshape(n,n))

