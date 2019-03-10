#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 15:21:08 2019

@author: Xu Liang

2017 Midterm Paper
"""

from math import tan, pi # For Question 3

# Question 3: Area of polygon
def area_r_polygon(n, s):
    return round((n * s**2)/(4 * tan(pi/n)), 3)


# Qustion 4: mysum
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


# Question 5: get_students
def get_students(students, course):
    taking = []
    for student in students:
        if course in student[1]:
            taking.append(student[0])
    return taking


# Question 6: SUTDBook
def get_nodes(fid):
    lines = fid.readlines()
    nodes = []
    for line in lines:
        try:
            nodes.append(tuple([int(line.split()[0]), int(line.split()[1])]))
        except:
            continue
    return nodes

def create_graph(nodes):
    graph = {}
    for node in nodes:
        try:
            graph[node[0]][node[1]] = 1
        except:
            graph[node[0]] = {}
            graph[node[0]][node[1]] = 1
        try:
            graph[node[1]][node[0]] = 1
        except:
            graph[node[1]] = {}
            graph[node[1]][node[0]] = 1
    return graph

def get_friends(G, node):
    return list(G[node].keys())

def suggested_new_friends(G, node):
    friends = get_friends(G, node)
    recs = {}
    for friend in friends:
        for ffriend in get_friends(G, friend):
            if ffriend not in friends:
                try:
                    recs[ffriend] += 1
                except:
                    recs[ffriend] = 1
    del recs[node]
    maximum = 0
    returnlist = [None, 0]
    for rec, connections in recs.items():
        if connections > maximum:
            returnlist[0] = [rec]
            maximum = connections
            returnlist[1] = connections
        elif connections == maximum:
            returnlist[0].append(rec)
    return returnlist


# Question 7: Number of Nonnegative Integer Solutions
def num_of_sol(n, var=5):
    if var == 1:
        return 1
    elif var == 2:
        return n+1
    sols = 0
    for i in range(0, n+1):
        sols += num_of_sol(n-i, var-1)
    return sols

