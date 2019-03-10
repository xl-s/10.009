#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 00:10:03 2019

@author: Xu Liang

2018 Midterm Paper
"""

from math import sqrt # For Question 3

# Question 3: Frustum
def area_square(s):
    return s**2

def vol_frustum(top_area, bottom_area, height):
    return height/3 * (top_area + bottom_area + sqrt(top_area + bottom_area))

def get_volume(s1, s2, height):
    return round(vol_frustum(area_square(s1), area_square(s2), height), 3)


# Question 4: Determinant
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


# Question 5: Newton-Raphson Method
def nroot(n, i, num):
    x = 1
    for j in range(i):
        x = x - (x**n - num)/(n * (x**(n-1)))
    return round(x, 3)

def nroot_complex(n, i, num):
    if n % 2:
        return nroot(n, i, -num)
    return nroot(n, i, -num) * 1j


# Question 6: MRT Path
def read_stations(f):
    stations = {}
    lines = f.readlines()
    for ind, line in enumerate(lines):
        if line[0] != '=' and line[0].strip():
            stations[lines[ind-1].strip().strip('=')] = line.strip().split(', ')
    return stations

def get_stationline(mrt):
    stations = {}
    for stops, line in zip(mrt.values(), mrt.keys()):
        for stop in stops:
            try:
                stations[stop].append(line)
            except:
                stations[stop] = [line]
    return stations

def get_interchange(stationline):
    interchanges = {}
    for station, line in zip(stationline.keys(), stationline.values()):
        if len(line) > 1:
            interchanges[station] = line
    return interchanges

def find_path(f, start, end):
    lines = read_stations(f)
    stations = get_stationline(lines)
    interchanges = get_interchange(stations)
    startlines = set(stations[start])
    endlines = set(stations[end])
    
    # Check for path on same line
    intersect = startlines & endlines
    if intersect:
        line = intersect.pop()
        si = lines[line].index(start)
        ei = lines[line].index(end)
        if ei > si:
            return lines[line][si:ei+1]
        else:
            return list(reversed(lines[line][ei:si+1]))
    
    # Check for path on adjacent line
    # Create list of interchange statiosn on same line
    startint = []
    endint = []
    for l, station in zip(interchanges.values(), interchanges.keys()):
        for line in l:
            if line in startlines:
                startint.append(station)
            if line in endlines:
                endint.append(station)
    
    # Generate paths through all interchanges and return the shortest one
    interchange = set(startint) & set(endint)
    paths = []
    if not interchange:
        return None
    while interchange:
        middle = interchange.pop()
        startline = (set(stations[middle]) & set(stations[start])).pop()
        endline = (set(stations[middle]) & set(stations[end])).pop()
        # Construct start line
        si = lines[startline].index(start)
        smi = lines[startline].index(middle)
        emi = lines[endline].index(middle)
        ei = lines[endline].index(end)
        if smi > si:
            path = lines[startline][si:smi]
        else:
            path = list(reversed(lines[startline][smi+1:si+1]))
        if ei > emi:
            path.extend(lines[endline][emi:ei+1])
        else:
            path.extend(list(reversed(lines[endline][ei:emi+1])))
        paths.append(path)
    return min(paths, key=len)
    

# Question 7: Decompose    
def decompose(pence, md=0):
    sols = 1
    if pence == 1:
        return sols
    denoms = [1, 2, 5, 10, 20, 50, 100, 200]
    for denom in denoms:
        if denom > pence or denom == md:
            break
        if denom == 1:
            continue
        elif denom == 2:
            sols += pence//denom
        else:
            for i in range(1, pence//denom + 1):
                sols += decompose(pence - denom*i, denom)
    return sols

