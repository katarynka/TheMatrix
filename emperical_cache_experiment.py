from typing import Callable , Any
import time
import numpy as np
from typing import List
import random
import sys
import csv

from experiments.measurement import measure

def generate_list_input(n: int) -> List[float] :
    return [random.randint(0,10000000) for x in range(n)]

def c_test(lst):
    dummy_variable = 0
    for i in range(100000):
        index = random.randint(0,len(lst)-1)
        dummy_variable += lst[index]
    return dummy_variable

def measure_time(f: Callable [[],Any])->float:
    start: float = time.time()
    f()
    end: float = time.time()
    return end - start


# ns = [2,4,8,16,32,64,128,256,512,1024,2048,4096]

ns = []
n = 1
for i in range(30):
    n = n*2
    ns.append(n)
print(ns)

for n in ns:
    lst = generate_list_input(n)
    print(n)
    n_nano = n*100000000
    nano_per_operation = n_nano / 100000
    np.ndarray(n)
    print(measure(lambda: c_test(lst)))


def write_csv(ns: List[int], res: np.ndarray, filename: str):
    with open(filename ,'w') as f:
        writer = csv.writer(f)
        for i in range(len(ns)):
            writer.writerow ([ns[i]] + res[i,:]. tolist ())
