#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 17:29:18 2019

@author: Xu Liang

2016 Midterm Paper
"""

from cmath import sqrt # For Question 3
from copy import deepcopy # For Question 6

# Question 3: Euclidean Norm
def norm(z1, z2, z3):
    return round(sqrt(z1 * z1.conjugate() + z2 * z2.conjugate() + z3 * z3.conjugate()).real, 3)


# Question 4: Factors
def factors(n):
    facs = []
    for i in range(1, n + 1):
        if n//i == n/i:
            facs.append(i)
    return sorted(facs)


# Question 5: Combinations
def combinations(n1, n2):
    initial = []
    for i in range(n1, n2+1):
        for j in range(i+1, n2+1):
            initial.append((i, j))
    return (sorted(list(set(initial))), len(set(initial)))


# Question 6: Gaussian Elimination
def readMatrix(f):
    matrix = []
    op = []
    stop = 0
    lines = f.readlines()
    for ind, line in enumerate(lines):
        if line.strip() == 'OP':
            stop = ind
            break
        try:
            matrix.append([float(num) for num in line.split()])
        except:
            continue
    for line in lines[stop:]:
        if line[0] in '12':
            op.append([num for num in line.split()])
    return {'matrix':matrix, 'op':op}

def mulRowByC(matOp, i, c):
    postOp = deepcopy(matOp)
    for j in range(len(matOp[i])):
        postOp[i][j] *= c
    return postOp

def addRowMulByC(matOp, i, c, j):
    postOp = deepcopy(matOp)
    for k in range(len(matOp[j])):
        postOp[j][k] += c * matOp[i][k]
    return postOp

def gaussElimination(data):
    read = readMatrix(data)
    ops = read['op']
    matrix = read['matrix']
    original = deepcopy(matrix)
    for op in ops:
        if op[0] == '1':
            matrix = mulRowByC(matrix, int(op[1]), float(op[2]))
        elif float(op[0]) == 2.0:
            matrix = addRowMulByC(matrix, int(op[1]), float(op[2]), int(op[3]))
    for i in range(len(original)):
        for j in range(len(original[i])):
            original[i][j] = round(original[i][j], 2)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = round(matrix[i][j], 2)
    return original, matrix


# Question 7: Max Product
def maxProductThree(num):
    negs = sorted([n for n in num if n < 0])
    pos = sorted([n for n in num if n > 0])
    print(pos, negs)
    if not pos:
        return negs[-1] * negs[-2] * negs [-3]
    if len(negs) == 1:
        if len(pos) == 2:
            return pos[0] * pos[1] * negs[0]
        return pos[-1] * pos[-2] * pos[-3]
    if not negs:
        return pos[-1] * pos[-2] * pos[-3]
    if len(pos) <= 2:
        return negs[-1] * negs[-2] * pos[-1]
    maxnegs = negs[-1] * negs[-2]
    maxpos = pos[-2] * pos[-3]
    if maxnegs > maxpos:
        return maxnegs * pos[-1]
    else:
        return maxpos * pos[-1]
        
