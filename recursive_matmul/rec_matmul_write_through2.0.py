import sys
sys.path.append("/home/gustavgyrst/Desktop/AA_Final/TheMatrix")
from matrix_implementations import *
import numpy as np



def recursive_multipliction_write_through_fun(A: Matrix, B: Matrix, C: Matrix) -> Matrix:
    
    n = A.rows()    
    
    if n == 1:
        C[0] += A[0]*B[0]
        return C
    
    else:
        #M0 C upper left                        a00             b00             c00
        a00b00 = recursive_multipliction_write_through_fun(A[:n//2,:n//2], B[:n//2,:n//2], C[:n//2,:n//2])
        #M1 C upper left                        a01             b10             c00
        a01b10 = recursive_multipliction_write_through_fun(A[:n//2,n//2:], B[n//2:,:n//2], C[:n//2,:n//2])
        
        #M2 C upper right                       a00             b01             c01
        a00b01 = recursive_multipliction_write_through_fun(A[:n//2,:n//2], B[:n//2,n//2:], C[:n//2,n//2:])
        #M3 C upper right                       a01             b11             c01
        a01b11 = recursive_multipliction_write_through_fun(A[:n//2,n//2:], B[n//2:,n//2:], C[:n//2,n//2:])
        
        #M4 C lower left                        a10             b00             c10
        a10b00 = recursive_multipliction_write_through_fun(A[n//2:,:n//2], B[:n//2,:n//2], C[n//2:,:n//2])
        #M5 C lower left                        a11             b10             c10
        a11b10 = recursive_multipliction_write_through_fun(A[n//2:,n//2:], B[n//2:,:n//2], C[n//2:,:n//2])
        
        #M6 C lower right                       a10             b01             c11
        a10b01 = recursive_multipliction_write_through_fun(A[n//2:,:n//2], B[:n//2,n//2:], C[n//2:,n//2:])
        #M7 C lower right                       a11             b11             c11
        a11b11 = recursive_multipliction_write_through_fun(A[n//2:,n//2:], B[n//2:,n//2:], C[n//2:,n//2:])

        return C
    


# M1 = Matrix(4,4, np.array([-5, 8, -7, -10, -1, -1, 3, -5, -2, -9, 5, -10, 6, -2, 2, -10]).reshape(4,4))
# M2 = Matrix(4,4, np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]).reshape(4,4))
# C = Matrix(M1.rows(), M1.rows())

# print(rec_matmul_write_through(M1,M2, C))










#ALTERNATIVE STRUCTURE 


def recursive_multipliction_write_through_fun(A: Matrix, B: Matrix, C: Matrix, m:int) -> Matrix:
    
    n = A.rows()    
    
    if n <= m:
        return elementary_multiplication_in_place(A,B,C)

    elif n == 1:
        C[0] += A[0]*B[0]
        return C
    
    else:
        #M0 C upper left                                        a00             b00             c00
        a00b00 = recursive_multipliction_write_through_fun(A[:n//2,:n//2], B[:n//2,:n//2], C[:n//2,:n//2])
        #M1 C upper left                                        a01             b10             c00
        a01b10 = recursive_multipliction_write_through_fun(A[:n//2,n//2:], B[n//2:,:n//2], C[:n//2,:n//2])
        
        #M2 C upper right                                       a00             b01             c01
        a00b01 = recursive_multipliction_write_through_fun(A[:n//2,:n//2], B[:n//2,n//2:], C[:n//2,n//2:])
        #M3 C upper right                                       a01             b11             c01
        a01b11 = recursive_multipliction_write_through_fun(A[:n//2,n//2:], B[n//2:,n//2:], C[:n//2,n//2:])
        
        #M4 C lower left                                        a10             b00             c10
        a10b00 = recursive_multipliction_write_through_fun(A[n//2:,:n//2], B[:n//2,:n//2], C[n//2:,:n//2])
        #M5 C lower left                                        a11             b10             c10
        a11b10 = recursive_multipliction_write_through_fun(A[n//2:,n//2:], B[n//2:,:n//2], C[n//2:,:n//2])
        
        #M6 C lower right                                       a10             b01             c11
        a10b01 = recursive_multipliction_write_through_fun(A[n//2:,:n//2], B[:n//2,n//2:], C[n//2:,n//2:])
        #M7 C lower right                                       a11             b11             c11
        a11b11 = recursive_multipliction_write_through_fun(A[n//2:,n//2:], B[n//2:,n//2:], C[n//2:,n//2:])

        return C
    

def recursive_multiplication_write_through(A: Matrix, B: Matrix, m: int)->Matrix:
    
    #Instructions:
        # Computes C=AB recursively using a write-through strategy. That
        # is, no intermediate copies are created; the matrix C is
        # initialized as the function is first called, and all updates
        # are done in-place in the recursive calls.
        
        # The parameter m controls such that when the subproblem size
        # satisfies n <= m, * an iterative cubic algorithm is called instead.

    #initializing C and getting the length of n
    n = A.rows()
    C = Matrix(A.rows(),A.rows())

    if n <= m:
        return elementary_multiplication_in_place(A,B,C)
    else:
        recursive_multipliction_write_through_fun(A,B,C,m)


