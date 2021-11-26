import sys
import numpy as np

#r = open("submatrix_test1.txt", 'r')
r = sys.stdin

n = int(r.readline())

i, j = [int(res) for res in r.readline().split(" ")]

#Creating the matrix with numpy
matrix = np.array([int(num) for num in r.readline().split(" ")]).reshape(n,n)



#The following code prints the specified submatrix

if ((i == 0) & (j == 0)): # taking left-upper corner
    for sub in matrix[:n//2,:n//2]:
        for line in sub:
            print(line, end=" ")
elif ((i == 0) & (j == 1)): # taking right upper corner
     for sub in matrix[:n//2,n//2:]:
            for line in sub:
                print(line, end=" ")
elif ((i == 1) & (j == 0)): # taking left lower corner
     for sub in matrix[n//2:,:n//2]:
            for line in sub:
                print(line, end=" ")
elif ((i == 1) & (j == 1)): # taking right lower corner
     for sub in matrix[n//2:,n//2:]:
            for line in sub:
                print(line, end=" ")



#input 
# 4
# 0 0

# 1  2  3  4 
# 5  6  7  8 
# 9  10 11 12 
# 13 14 15 16

#Expected output test1 submatrix
#1 2 
#5 6

