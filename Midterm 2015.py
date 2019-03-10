#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 18:52:21 2019

@author: Xu Liang

2015 Midterm Paper
"""

# Question 3: comp
def comp(x):
    return x**3 + 4 * x**2 + 6 * x + 1


# Question 4: Generate List
def genList(n1, n2):
    retlist = []
    for i in range(n1, n2+1):
        if i // 3 == i/3:
            retlist.append(i)
    return retlist


# Question 5: Matrix Addition
def matAdd(A, B):
    m, n = len(A), len(A[0])
    C = []
    for i in range(m):
        C.append([])
        for j in range(n):
            C[i].append(A[i][j] + B[i][j])
    return C


# Question 6: Schedule
def getSchedule(f):
    schedule = {}
    for line in f:
        if line[0] not in '1234567890':
            currentKey = line.strip()
        else:
            schedule.setdefault(currentKey, []).append(tuple([int(elm) for elm in line.strip().split()]))
    return schedule

def findLength(dictSchedule):
    lengths = {}
    for day, times in dictSchedule.items():
        lengths[day] = 0
        for time in times:
            lengths[day] += time[1] - time[0]
    return lengths

def findConflict(dictSchedule):
    sortedSche = {}
    conflicts = {}
    for day, times in dictSchedule.items():
        sortedSche[day] = sorted(times, key=lambda time: time[0])
        conflicts[day] = False
    for day, times in sortedSche.items():
        end = 0
        for time in times:
            if time[0] < end:
                conflicts[day] = True
                break
            end = time[1]
    return conflicts
        

# Question 7: Pixel Count
def countLitPixel(cx, cy, r):
    # 4 times of litpixels in one corner.
    count = 0
    for i in range(r):
        for j in range(r):
            if r > (i**2 + j**2)**0.5:
                count += 1
            else:
                break
    return 4 * count

