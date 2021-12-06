import sys
#sys.path.append("/home/katarzyna/Documents/school/applied_algo/exam/TheMatrix")
sys.path.append("/home/gustavgyrst/Desktop/AA_Final/TheMatrix")

from matrix_implementations import *
from benchmark import *
from measurement import *



tiled_N = 1024
s_list = [2,4,8,16,32,64,128,256,512]
args1 = [Matrix(tiled_N,tiled_N, np.array(generate_input(tiled_N)).reshape(tiled_N,tiled_N)) for s in s_list]
args2 = [Matrix(tiled_N,tiled_N, np.array(generate_input(tiled_N)).reshape(tiled_N,tiled_N)) for s in s_list]

res_tiled = benchmark_tiled(tiled_multiplication, args1 , args2, s_list, N)
print(res_tiled)


def write_csv_tiled(ns: List[int], res: np.ndarray ,
            filename: str):
    with open(filename ,'w') as f:
        writer = csv.writer(f)
        for i in range(len(s_list)):
            writer.writerow ([s_list[i]] + res[i,:]. tolist ())

write_csv_tiled(ns, res_tiled, "tiled.csv")
