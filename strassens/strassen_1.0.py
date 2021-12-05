import numpy as np
#https://www.youtube.com/watch?v=OSelhO6Qnlc



def strassen(A, B):
    
    n = len(A)
    
    if n == 1:
        C = A*B
        return C
    
    else:
        
        C = np.zeros(A.shape, dtype=A.dtype)
        
        C00 = C[:n//2,:n//2]
        C01 = C[:n//2,n//2:]
        C10 = C[n//2:,:n//2]
        C11 = C[n//2:,n//2:]
        
        
        # P1 = A00 + A11
        P1 = A[:n//2,:n//2] + A[n//2:,n//2:]
        # P2 = A10 + A11
        P2 = A[n//2:,:n//2] + A[n//2:,n//2:]
        # P3 = A00
        P3 = A[:n//2,:n//2]
        # P4 = A11
        P4 = A[n//2:,n//2:]
        # P5 = A00 + A01
        P5 = A[:n//2,:n//2] + A[:n//2,n//2:]
        # P6 = A10 - A00
        P6 = A[n//2:,:n//2] - A[:n//2,:n//2]
        # P7 = A01 - A11
        P7 = A[:n//2,n//2:] - A[n//2:,n//2:]
        
        # Q1 = B00 + B11
        Q1 = B[:n//2,:n//2] + B[n//2:,n//2:]
        # Q2 = B00
        Q2 = B[:n//2,:n//2]
        # Q3 = B01 - B11 
        Q3 = B[:n//2,n//2:] - B[n//2:,n//2:]
        # Q4 = B10 - B00
        Q4 = B[n//2:,:n//2] - B[:n//2,:n//2]
        # Q5 = B11
        Q5 = B[n//2:,n//2:]
        # Q6 = B00 + B01
        Q6 = B[:n//2,:n//2] + B[:n//2,n//2:]
        # Q7 = B10 + B11
        Q7 = B[n//2:,:n//2] + B[n//2:,n//2:]
            
        # Then compute Mi = Pi*Qi by a recursive application of the function
        M1 = strassen(P1,Q1)
        M2 = strassen(P2,Q2)
        M3 = strassen(P3,Q3)
        M4 = strassen(P4,Q4)
        M5 = strassen(P5,Q5)
        M6 = strassen(P6,Q6)
        M7 = strassen(P7,Q7)
        
        # Following the recipe from the slides:
        C00[:] = M1 + M4 - M5 + M7
        C01[:] = M3 + M5
        C10[:] = M2 + M4
        C11[:] = M1 - M2 + M3 + M6

        return C

M10 = np.array([ [1,1,1,1],
                 [2,2,2,2],
                 [3,3,3,3],
                 [4,4,4,4]])

M20 = np.array([ [1,1,1,1],
                 [2,2,2,2],
                 [3,3,3,3],
                 [4,4,4,4]])

print(strassen(M10, M20))

