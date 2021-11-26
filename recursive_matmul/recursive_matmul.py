import numpy as np

def create_empty_C(n):
    return np.array([[0]*n]*n)


#Trying with a C 
def rec_matmul(A,B,C):
            
    n = len(A)
    
    if n == 1:
        print(A)
        print(B)
        print(A*B)
        C += A*B
        return C
    
    else:
        #M0 C upper left        a00               b00            c00
        a00b00 = rec_matmul(A[:n//2,:n//2], B[:n//2,:n//2], C[:n//2,:n//2])
        #M1 C upper left        a01               b10            c00
        a01b10 = rec_matmul(A[:n//2,n//2:], B[n//2:,:n//2], C[:n//2,:n//2])
        
        #M2 C upper right        a00              b01            c01
        a00b01 = rec_matmul(A[:n//2,:n//2], B[:n//2,n//2:], C[:n//2,n//2:])
        #M3 C upper right        a01              b11            c01
        a01b11 = rec_matmul(A[:n//2,n//2:], B[n//2:,n//2:], C[:n//2,n//2:])
        
        #M4 C lower left         a10              b00            c10
        a10b00 = rec_matmul(A[n//2:,:n//2], B[:n//2,:n//2], C[n//2:,:n//2])
        #M5 C lower left          a11             b10            c10
        a11b10 = rec_matmul(A[n//2:,n//2:], B[n//2:,:n//2], C[n//2:,:n//2])
        
        #M6 C lower right         a10             b01            c11
        a10b01 = rec_matmul(A[n//2:,:n//2], B[:n//2,n//2:], C[n//2:,n//2:])
        #M7 C lower right         a11             b11            c11
        a11b11 = rec_matmul(A[n//2:,n//2:], B[n//2:,n//2:], C[n//2:,n//2:])

    print(C)

      
# Ways to make it print properly: 
# use the numpy print in c order etc tools / or Mattis library tools

#Test
test = np.array([[1,1,1,1],
                 [2,2,2,2],
                 [3,3,3,3],
                 [4,4,4,4]])

test2 = np.array([[1,1,1,1],
                 [2,2,2,2],
                 [3,3,3,3],
                 [4,4,4,4]])


test_01a = np.array([[4,8],
                    [5,-7]])
test_01b = np.array([[-9,-1],
                     [-1,0]])


C = create_empty_C(2)
C2 = create_empty_C(4)

#rec_matmul(test_01a, test_01b)
rec_matmul(test_01a,test_01b, C)

rec_matmul(test,test2, C2)


# [[10 10 10 10]
#  [20 20 20 20]
#  [30 30 30 30]
#  [40 40 40 40]]

res = np.matmul(test, test2)

#print(res)

# Look into these stacks
#np.hstack()
#np.vstack()

#For the copying variant


# The advantage of this auxiliary version is that is based on the concept of immutability (not having a base structure for C that is filled with 0)
# This is important because the version with the C initiated i/substitution occuring
# In the copying variant we never make a point move - we instead make auxiliary submatrices that then can be stacked together (v-stack or hstack)
