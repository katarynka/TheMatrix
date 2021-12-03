import numpy as np
import sys

path_of_testcase_file = "/home/gustavgyrst/Desktop/AA_Final/TheMatrix/recursive_matmul/rec_test2.txt"

# copy/uncopy this one out to run the files from the path with a testfile
r = open(path_of_testcase_file, 'r')

# copy/uncopy to run in the terminal
#r = sys.stdin

#Reading the input
n = int(r.readline())
A_lst = [int(x) for x in r.readline().strip().split(" ")]
B_lst = [int(x) for x in r.readline().strip().split(" ")]


#Convertion to_matrix from the list given
def to_matrix(lst, n, m, order):
    
    A = list()
    for i in range(n): # Creating the empty matrix
        A.append([0]*m) 

    for k in range(len(lst)):
        if order == 'C':
            A[k//m][k%m] = lst[k] #k%m moves by row first and // is whole number division, which makes the rows jump correct everytime the three 3 column entries are reached
        elif order == 'F':
            A[k%n][k//n] = lst[k] #opposite structure for F 
            
    return A

def recursive_multiplication_copying(A,B):
            
    n = len(A)
    
    [print(i, end=" ") for i in A.flatten()]
    print()
    [print(i, end=" ") for i in B.flatten()]
    print()
    
    if n == 1:
        C = A*B   
        # print(' '.join(map(str,A.flatten())))
        # print(' '.join(map(str,B.flatten())))
        print(' '.join(map(str,(A*B).flatten())))
        
        return C
    
    else:
        
        C = np.zeros(A.shape, dtype=A.dtype)
        
        C00 = C[:n//2,:n//2]
        C01 = C[:n//2,n//2:]
        C10 = C[n//2:,:n//2]
        C11 = C[n//2:,n//2:]
        
        #M0 C upper left                            a00               b00           returns c00
        a00b00 = recursive_multiplication_copying(A[:n//2,:n//2], B[:n//2,:n//2])
        #M1 C upper left                            a01               b10           returns c00
        a01b10 = recursive_multiplication_copying(A[:n//2,n//2:], B[n//2:,:n//2])
        
        #M2 C upper right                           a00              b01            returns c01
        a00b01 = recursive_multiplication_copying(A[:n//2,:n//2], B[:n//2,n//2:])
        #M3 C upper right                           a01              b11            returns c01
        a01b11 = recursive_multiplication_copying(A[:n//2,n//2:], B[n//2:,n//2:])
        
        #M4 C lower left                            a10              b00            returns c10
        a10b00 = recursive_multiplication_copying(A[n//2:,:n//2], B[:n//2,:n//2])
        #M5 C lower left                            a11             b10            returns c10
        a11b10 = recursive_multiplication_copying(A[n//2:,n//2:], B[n//2:,:n//2])
        
        #M6 C lower right                           a10             b01            returns c11
        a10b01 = recursive_multiplication_copying(A[n//2:,:n//2], B[:n//2,n//2:])
        #M7 C lower right                           a11             b11            returns c11
        a11b11 = recursive_multiplication_copying(A[n//2:,n//2:], B[n//2:,n//2:])

        
        C00[:] = a00b00 + a01b10  #M0 + M1
        C01[:] = a00b01 + a01b11 #M2 + M3
        C10[:] = a10b00 + a11b10 #M4 + M5
        C11[:] = a10b01 + a11b11 #M6 + M7
        
        [print(i, end=" ") for i in C.flatten()]
        print()
        
        return C

A2d = to_matrix(A_lst, n, n,"C")
B2d = to_matrix(B_lst,n,n, "C")

#Converting into np.arrays:
A = np.array(A2d)
B = np.array(B2d)

recursive_multiplication_copying(A,B)

















# test = np.array([[1,1,1,1],
#                  [2,2,2,2],
#                  [3,3,3,3],
#                  [4,4,4,4]])

# test2 = np.array([[1,1,1,1],
#                  [2,2,2,2],
#                  [3,3,3,3],
#                  [4,4,4,4]])


# recursive_multiplication_copying(test, test2)


# test2a = np.array([[-5, 8, -7,-10],
#                    [-1, -1, 3, -5],
#                    [-2, -9, 5, -10],
#                    [6,-2, 2, -10]])

# test2b = np.array( [[4, -7, -2, -4],
#                     [6, 6, -8, 1], 
#                     [-10,1, 2, 1],    
#                     [-6, -9, -10, -9]])

# recursive_multiplication_copying(test2a, test2b)