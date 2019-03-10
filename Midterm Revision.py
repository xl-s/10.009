# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 16:44:14 2019

@author: Xu Liang

Mid Term Revision
"""

# Question 1: Determinant
def determinant(matrix):
    n = len(matrix)
    if(n != len(matrix[0]) or n not in [1, 2, 3]):
        return None
    if n == 1:
        return matrix[0][0]
    elif n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    elif n == 3:
        return matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]) + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])


# Question 2: Newton-Raphson Method
def nroot(n, i, num):
    x = 1
    for j in range(i):
        x = x - (x**n - num)/(n * (x**(n-1)))
    return round(x, 3)

def nroot_complex(n, i, num):
    if n % 2:
        return nroot(n, i, -num)
    return nroot(n, i, -num) * 1j
    

# Question 3: mysum
def mysum(a, b, limit):
    if type(a) != int or type(b) != int or a <= 0 or b <= 0:
        return 'Wrong input'
    multiples = []
    maxa = limit//a
    maxb = limit//b
    for i in range(1, maxa+1):
        if a*i < limit:
            multiples.append(a*i)
    for j in range(1, maxb+1):
        if b*j < limit:
            multiples.append(b*j)
    return sum(set(multiples))


# Question 4: get_students
def get_students(students, course):
    taking = []
    for student in students:
        if course in student[1]:
            taking.append(student[0])
    return taking


# Question 5: factors
def factors(n):
    facs = []
    for i in range(1, n + 1):
        if n//i == n/i:
            facs.append(i)
    return sorted(facs)


# Question 6: combinations
def combinations(n1, n2):
    initial = []
    for i in range(n1, n2+1):
        for j in range(i+1, n2+1):
            initial.append((i, j))
    return (sorted(list(set(initial))), len(set(initial)))


# Question 7: genList
def genList(n1, n2):
    retlist = []
    for i in range(n1, n2+1):
        if i // 3 == i/3:
            retlist.append(i)
    return retlist


# Question 8: matAdd
def matAdd(A, B):
    m, n = len(A), len(A[0])
    C = []
    for i in range(m):
        C.append([])
        for j in range(n):
            C[i].append(A[i][j] + B[i][j])
    return C

