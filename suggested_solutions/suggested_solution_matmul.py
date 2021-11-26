#!/usr/bin/env python3

import sys


def matmul(A,B):
    n = len(A)
    m = len(A[0])
    assert len(B) == m
    p = len(B[0])
    C = list()
    for i in range(n):
        C.append([0]*p)

    for i in range(n):
        for j in range(p):
            for k in range(m):
                C[i][j] += A[i][k]*B[k][j]
    return C


def array_to_matrix(array, n, m, order):
    assert len(array) == n*m
    A = list()
    for i in range(n):
        A.append([0]*m)
    for k in range(n*m):
        if order == 'C':
            A[k//m][k%m] = array[k]
        elif order == 'F':
            A[k%n][k//n] = array[k]
    return A

def matrix_to_array(A, n, m, order):
    array = list()
    if order == 'C':
        for i in range(n):
            for j in range(m):
                array.append(A[i][j])
    elif order == 'F':
        for j in range(m):
            for i in range(n):
                array.append(A[i][j])
    return array



if __name__ == '__main__':
    n, m, p, order = sys.stdin.readline().split()
    n = int(n)
    m = int(m)
    p = int(p)

    array = list(map(int,sys.stdin.readline().split()))
    A = array_to_matrix(array, n, m, order)

    array = list(map(int,sys.stdin.readline().split()))
    B = array_to_matrix(array, m, p, order)

    C = matmul(A,B)
    
    print(' '.join(map(str,matrix_to_array(C,n,p,order))))
