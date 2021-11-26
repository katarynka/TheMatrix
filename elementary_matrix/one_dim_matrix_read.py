import sys


r = sys.stdin
# for line in r:
#     print(line)
    

#r = open("text.txt", 'r')

m, n, style = r.readline().strip().split(" ")

m = int(m)
n = int(n)

matrix = r.readline().strip().split(" ")


for line in r:
    i,j = [int(x) for x in line.strip().split(" ")]
    if style == 'C':
        #This way we get the row-styled position of the given element
        print(matrix[i*n + j]) 
    else:
        print(matrix[j*m + i])
        

    

