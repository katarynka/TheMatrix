import sys

#r = sys.stdin
# for line in r:
#     print(line)


string = "hel"
string.isnumeric

r = open("test_matmul.txt", 'r')

l, m, n, style = [int(x) if x.isnumeric() else x for x in r.readline().strip().split(" ")]


A = [int(x) for x in r.readline().strip().split(" ")]
B = [int(x) for x in r.readline().strip().split(" ")]

lst = []

if style =='C':
    for i in range(l):
        for k in range(n):
            res = 0
            for j in range(m):
                A_cell = A[i*m + j] #fetches from A by row
                B_cell = B[j*n + k] #fetches from B by column
                res += A_cell * B_cell # The result of the matmul for a given cell * cell
            lst.append(res) #result combined to be pasted in the result
            
else:
    pass


for i in lst:
    print(i, end=" ")
    
#Expected output
# 19 22 43 50

#Test2 Fortran expected output
#23 34 31 46


#Earlier Implementation
# else:
#     for k in range(n):
#         for i in range(l):
#             res = 0
#             for j in range(m):
#                 B_cell = B[i*n + j]
#                 A_cell = A[j*m + i]
#                 res += A_cell * B_cell
#             lst.append(res)

