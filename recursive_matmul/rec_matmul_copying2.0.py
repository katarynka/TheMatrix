import numpy as np
import sys
sys.path.append("/home/gustavgyrst/Desktop/AA_Final/TheMatrix")
from matrix_implementations import *

M1 = Matrix(4,4, np.array([-5, 8, -7, -10, -1, -1, 3, -5, -2, -9, 5, -10, 6, -2, 2, -10]).reshape(4,4))
M2 = Matrix(4,4, np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]).reshape(4,4))


#Attempt to implement the operations using the numpy library 

def recursive_multiplication_copying(A:Matrix , B:Matrix) -> Matrix:
            
    n = A.rows()
    
    if A.rows().__eq__(1):
    
        C = A[0]*B[0]
        return C
    
    else:
        
        C = Matrix(A.rows(), A.cols())
        
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

        
        C00[:] = a00b00 + a01b10 #M0 + M1
        C01[:] = a00b01 + a01b11 #M2 + M3
        C10[:] = a10b00 + a11b10 #M4 + M5
        C11[:] = a10b01 + a11b11 #M6 + M7
        
        return C


print(recursive_multiplication_copying(M1, M2))




