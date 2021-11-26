import sys

#https://www.programiz.com/python-programming/operators
#Really cool overview of python linguistics


#r = open("test_matmul.txt", 'r')
r = sys.stdin

n, m, p, order = [int(x) if x.isnumeric() else x for x in r.readline().strip().split(" ")]


A_lst = [int(x) for x in r.readline().strip().split(" ")]
B_lst = [int(x) for x in r.readline().strip().split(" ")]

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

def to_matrix_original(lst, row, col, order):
    A = list()
    for i in range(row):
        A.append([0]*col)
    
    if order == 'C':
        for i in range(row):
            for j in range(col):
                A[i][j] = lst[i*col + j]
    elif order == "F":
        for j in range(col):
            for i in range(row):
                A[i][j] = lst[j*row + i]
    return A
                
def to_lst_original(matrix, row, col, order):
    lst = list()
    if order == 'C':
        for i in range(row):
            for j in range(col):
                lst.append(matrix[i][j])
    elif order == 'F':
        for j in range(col):
            for i in range(row):
                lst.append(matrix[i][j])
    return lst

def matrix_multiplication(A,B):
    
    n = len(A); m = len(A[0]); p = len(B[0])
    
    C = list()
    for i in range(n):
        C.append([0]*p)

    #follows the pseudo-code from class.
    for i in range(n):
        for j in range(p):
            for k in range(m):
                C[i][j] += A[i][k]*B[k][j]
    return C


A = to_matrix_original(A_lst, n, m, order) #n=row, m=col for A
B = to_matrix_original(B_lst, m, p, order) #m=row, p=col for B

result = matrix_multiplication(A,B)

result_as_lst = to_lst_original(result, n, p, order)

for number in result_as_lst:
    print(number, end=" ")




# #Tests            
# test1 = to_matrix_original([1,2,3,4,5,6], 3, 2, 'C')
# test2 = to_matrix_original([1,2,3,4,5,6], 3, 2, 'F')
# test3 = to_matrix_original([1,2,3], 1, 3, 'F')

# test12 = to_matrix([1,2,3,4,5,6], 3,2, 'C')
# test22 = to_matrix([1,2,3,4,5,6], 3,2, 'F')
# test3 = to_matrix([1,2,3], 1, 3, 'F')

# lst = to_lst_original(test1, 3, 2, 'C')
# print(lst)