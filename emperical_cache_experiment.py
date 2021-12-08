from typing import Callable , Any
import time
import numpy as np
from typing import List
import random
import sys

from experiments.measurement import measure

def generate_list_input(n: int) -> List[float] :
    return [random.randint(0,1000000) for x in range(n)]

def c_test(lst):
    dummy_lst = []
    for i in range(100000):
        index = random.randint(0,len(lst)-1)
        dummy_variable = lst[index]
        dummy_lst.append(dummy_variable)
    return dummy_lst

def measure_time(f: Callable [[],Any])->float:
    start: float = time.time()
    f()
    end: float = time.time()
    return end - start



ns = [2,4,8,16,32,64,128,256,512,1024,2048,4096]

for n in ns:
    lst = generate_list_input(n**2)
    print(n*n)
    print(measure(lambda: c_test(lst)))
