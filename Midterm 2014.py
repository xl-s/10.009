# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 19:41:09 2019

@author: Xu Liang

2014 Midterm Paper
"""

# Question 1: Length Difference
def stc(s1, s2):
    return abs(len(s1) - len(s2))


# Question 2: Sum Difference
def sumVal(d):
    return sum([val for key, val in d.items() if key < 3])


# Question 3: Count
def count(a, b, c):
    return True if max(0, b - a) > max(0, c - b) else False


# Question 4: MRT
def getMRT(f):
    data = {}
    for line in f:
        data[line.split(',')[0]] = line.strip().split(',')[1:]
    return data

def distance(d, s):
    if not s:
        return -2
    elif len(s.split(',')) == 1:
        return -1
    stations = s.split(',')
    for line, stops in d.items():
        if stations[0] in stops and stations[1] in stops:
            return abs(stops.index(stations[0]) - stops.index(stations[1]))
    return -1


# Question 5: Matrix
class Matrix:
    def __init__(self, m, s='Matrix A', f='%6.2f'):
        self.name = s
        self.format = f
        self.matrix = m
        
    def __str__(self):
        string = ''
        string += '{}: Rows: {} Columns: {}\n'.format(self.name, len(self.matrix), len(self.matrix))
        for row in self.matrix:
            for elm in row:
                string += self.format % elm + '\t'
            string += '\n'
        return string
    
    def diag(self):
        for i in range(len(self.matrix)):
            if self.matrix[i][i] == 0:
                return False
        return True
    
    def upperDiag(self):
        for i in range(len(self.matrix) - 1):
            if self.matrix[i][i+1] == 0:
                return False
        return True
    
    def lowerDiag(self):
        for i in range(1, len(self.matrix)):
            if self.matrix[i][i-1] == 0:
                print(i)
                return False
        return True
    
    def triDiag(self):
        n = len(self.matrix)
        if not self.diag() or not self.upperDiag() or not self.lowerDiag():
            return False
        for i in range(n):
            for j in range(min(2+i,5),n):
                if self.matrix[i][j] != 0:
                    return False
            for j in range(0, max(i-1,0)):
                if self.matrix[i][j] != 0:
                    return False
        return True
                
        