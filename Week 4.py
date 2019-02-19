# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 08:35:19 2019

@author: Xu Liang

Week 4 Problem Set
"""

from random import randint, random # For Exercise 3, Exercise 4 and Exercise 5

# Cohort Sessions 2
def compound_value_months(saving, interest, months):
    cumulative = 0
    for i in range(months):
        cumulative += saving
        cumulative *= (1 + interest/12)
    return round(cumulative, 2)


# Cohort Sessions 3
def find_average(items):
    average = []
    alltotal = 0
    allitems = 0
    for item in items:
        total = 0
        for subitem in item:
            total += subitem
            alltotal += subitem
            allitems += 1
        if(len(item)):
            average.append(total/len(item))
        else:
            average.append(0)
    allaverage = alltotal/allitems
    return average, allaverage


# Cohort Sessions 4
def transpose_matrix(matrix):
    n = len(matrix)
    m = len(matrix[0])
    transposed = []
    for i in range(m):
        transposed.append([])
        for j in range(n):
            transposed[i].append(matrix[j][i])
    return transposed


# Cohort Sessions 5
def get_details(name, key, items):
    index = None
    for indx, item in enumerate(items):
        if(item.get("name") == name):
            index = indx
            break
    if(index == None):
        return None
    return items[index].get(key)


# Cohort Sessions 6
def get_base_counts(DNA):
    DNAs = {'A': 0, 'C':0, 'G': 0, 'T':0}
    for dna in DNA:
        if dna in DNAs:
            DNAs[dna] += 1
        else:
            return 'The input DNA string is invalid'
    return DNAs


# Homework 1
def f_to_c(f):  
    c = (f - 32) * 5/9
    return round(c, 1)

def f_to_c_approx(f):
    c = (f - 30) / 2
    return round(c, 1)

def get_conversion_table_a(values=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]):
    table = []
    for indx, value in enumerate(values):
        table.append([])
        table[indx].append(value)
        table[indx].append(f_to_c(value))
        table[indx].append(f_to_c_approx(value))
    return table

def get_conversion_table_b(values=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]):
    return transpose_matrix(get_conversion_table_a(values))
    

# Homework 2
def max_list(inlist):
    outlist = []
    for item in inlist:
        maximum = item[0]
        for subitem in item:
            if(subitem > maximum):
                maximum = subitem
        outlist.append(maximum)
    return outlist


# Homework 3
def multiplication_table(n):
    if(n < 1):
        return None
    table = []
    for i in range(1, n+1):
        row = []
        for j in range(1, n+1):
            row.append(i*j)
        table.append(row)
    return table


# Homework 4
def most_frequent(items):
    counts = {}
    for item in items:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    maxlist = []
    maximum = 0
    for num in counts:
        if(counts[num] > maximum):
            maxlist = [num]
            maximum = counts[num]
        elif(counts[num] == maximum):
            maxlist.append(num)
    return maxlist


# Homework 5
def diff(poly):
    dpoly = {}
    for coef in poly:
        if(coef):
            dpoly[(coef - 1)] = coef * poly[coef]
    return dpoly


# Exercise 2
def interlock(word1, word2, word3):
    if(word1 == '' or word2 == '' or not len(word1) == len(word2)):
        return False
    word = ''
    for indx, char in enumerate(word1):
        word = word + char
        word = word + word2[indx]
    if(word == word3):
        return True
    else:
        return False
    

# Exercise 3
def throw_dice(n, nexp):
    totalsixes = 0
    for i in range(nexp):
        for j in range(n):
            if(randint(1, 6) == 6):
                totalsixes += 1
                break
    probability = totalsixes/nexp
    return round(probability, 2)


# Exercise 4
def pi_approx_by_monte_carlo(n):
    counts = 0 # counts / n = pi/4
    for i in range(n):
        if((random()**2 + random()**2)**0.5 <= 1):
            counts += 1
    piapprox = 4 * counts / n
    return piapprox


# Exercise 5
def game(r, n):
    net = 0
    for i in range(n):
        net -= 1
        if((randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6)) < 9):
            net += r
    if(net > n):
        return True
    else:
        return False


# Exercise 6
def approx_ode2(h, t0, y0, tn):
    steps = int((tn - t0) / h)
    yt = y0
    t = t0
    for i in range(steps):
        yt += h * (0.5 * f(t, yt) + 0.5 * f(t+h, yt) + h * f(t, yt))
        t += h
    return yt

def f(t, y):
    return 4 - t + 2 * y

