#Trying with a C 
def rec_matmul_c(A,B):
            
    n = len(A)
    
    if n == 1:
        print(A)
        print(B)
        print(A*B)
        C += A*B
        return C
    
    else:
        #M0 C upper left        a00               b00            c00
        a00b00 = rec_matmul_c(A[:n//2,:n//2], B[:n//2,:n//2])
        #M1 C upper left        a01               b10            c00
        a01b10 = rec_matmul_c(A[:n//2,n//2:], B[n//2:,:n//2])
        
        #M2 C upper right        a00              b01            c01
        a00b01 = rec_matmul_c(A[:n//2,:n//2], B[:n//2,n//2:])
        #M3 C upper right        a01              b11            c01
        a01b11 = rec_matmul_c(A[:n//2,n//2:], B[n//2:,n//2:])
        
        #M4 C lower left         a10              b00            c10
        a10b00 = rec_matmul_c(A[n//2:,:n//2], B[:n//2,:n//2])
        #M5 C lower left          a11             b10            c10
        a11b10 = rec_matmul_c(A[n//2:,n//2:], B[n//2:,:n//2])
        
        #M6 C lower right         a10             b01            c11
        a10b01 = rec_matmul_c(A[n//2:,:n//2], B[:n//2,n//2:])
        #M7 C lower right         a11             b11            c11
        a11b11 = rec_matmul_c(A[n//2:,n//2:], B[n//2:,n//2:])

    print(C)

