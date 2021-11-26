#!/usr/bin/env python3

import numpy as np
import sys

#r = sys.stdin 
r = open("submatrix_test1.txt", 'r')

n = int(r.readline())
i, j = map(int,r.readline().split())
A = np.array(list(map(int,r.readline().split()))).reshape(n,n)
A = A[:n//2,:] if i == 0 else A[n//2:,:]
A = A[:,:n//2] if j == 0 else A[:,n//2:]    
print(' '.join(map(str,A.ravel())))