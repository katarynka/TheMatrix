import sys
sys.path.append("/home/gustavgyrst/Desktop/AA_Final/TheMatrix")
from typing import List , Tuple , Optional , Dict , Callable , Any
import time
import numpy as np
from typing import List
import random
import csv
from experiments.measurement import *

def generate_list_input(n: int) -> List[float] :
    return [random.randint(0,100000) for x in range(n)]

def cache_test(lst):
    dummy_variable = 0
    for i in range(10000):
        index = random.randint(0,len(lst)-1)
        dummy_variable += lst[index]
    return dummy_variable

def measure_time(f: Callable [[],Any])->float:
    start: float = time.time()
    f()
    end: float = time.time()
    return end - start

def create_ns(ns_size):
    n = 1
    ns = []
    for i in range(ns_size):
        n = n*2
        ns.append(n)
    return ns


def benchmark_cache(f, ns: list, N: int)->np.ndarray:
    m: int = len(ns)
    M: np.ndarray = np.zeros ((m,N)) # measurements
    for i in range(len(ns)):
        lst = generate_list_input(ns[i])
        print("current test:", + ns[i])
        for j in range(N):
            res = measure(lambda: f(lst))
            res_nano = res*1000000000
            res_nano_per_operation = res_nano/10000
            M[i,j] = res_nano_per_operation
    means = np.mean(M,axis =1).reshape(m,1)
    stdevs = np.std(M,axis=1,ddof =1).reshape(m,1)
    return np.hstack([means , stdevs])


def write_csv(ns: List[int], res: np.ndarray, filename: str):
    with open(filename ,'w') as f:
        writer = csv.writer(f)
        for i in range(len(ns)):
            writer.writerow ([ns[i]] + res[i,:]. tolist ())


ns = create_ns(30)

# for n in ns:
#     lst = generate_list_input(n)
#     print(n)
#     n_nano = n*100000000
#     nano_per_operation = n_nano / 100000
#     print(measure(lambda: c_test(lst)))

cache_res = benchmark_cache(cache_test, ns, 5)

write_csv(ns, cache_res, "cache_test.csv")