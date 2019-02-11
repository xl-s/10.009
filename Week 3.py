# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 00:09:49 2019

@author: Xu Liang

Week 3 Problem Set
"""

from math import exp, factorial # For Homework 4 and Exercise 3

# Cohort Sessions 1
def list_sum(values):
    sum = 0.0
    for value in values:
        sum += value
    return sum


# Cohort Sessions 2
def minmax_in_list(values):
    if(values == []):
        return None, None
    maximum = values[0]
    minimum = values[0]
    for value in values:
        if(value > maximum):
            maximum = value
        if(value < minimum):
            minimum = value
    return minimum, maximum


# Cohort Sessions 3
def is_palindrome(num):
    num = list(str(num))
    half = len(num) // 2
    i = 0
    while(i <= half):
        if(num[i] != num[-(i+1)]):
            return False
        i += 1
    return True


# Homework 1
def temp_convert(unit, value):
    if(unit == 'C'):
        return fahrenheit_to_celsius(value)
    elif(unit == 'F'):
        return celsius_to_fahrenheit(value)
    else:
        return None

def fahrenheit_to_celsius(f):  
    c = (f - 32) * 5/9
    return c

def celsius_to_fahrenheit(c):
    f = c * 9/5 + 32
    return f


# Homework 2
def get_even_list(values):
    even = []
    for value in values:
        if(value // 2 == value / 2):
            even.append(value)
    return even


# Homework 3
def is_prime(value):
    if(value == 1 or value < 0):
        return False
    for i in range(2, value//2 + 1):
        if(not (value % i)):
            return False
    return True


# Homework 4
def approx_ode(h, t0, y0, tn):
    steps = int((tn - t0) / h)
    yt = y0
    t = t0
    for i in range(steps):
        yt = yt + h * (3 + exp(-t) - 0.5 * yt)
        t += h
    return yt


# Exercise 1
def may_ignore(value):
    if(str(type(value)) == "<class 'int'>"):
        return value + 1
    else:
        return None
    

# Exercise 2
def my_reverse(values):
    newlist = []
    for value in values:
        newlist.insert(0, value)
    return newlist


# Exercise 3
def approx_pi(n):
    constant = (2 * (2**0.5)) / 9801
    summation = 0
    for k in range(n):
        summation += (factorial(4*k)*(1103+26390*k))/((factorial(k))**4 * 396**(4*k))
    pi = 1/(summation * constant)
    return pi


# Exercise 4
def gcd(a, b):
    if(a > b):
        return gcd(a-b, b)
    elif(b > a):
        return gcd(a, b-a)
    elif(a == b):
        return a
    

# Exercise 5
def simpsons_rule(f, n, a, b):
    h = (b-a)/n
    sum1, sum2 = 0, 0
    for j in range(1, int(n/2)):
        sum1 += f(a+2*j*h)
    for j in range(1, int(n/2)+1):
        sum2 += f(a+(2*j-1)*h)
    integral = h/3 * (f(a) + 2 * sum1 + 4 * sum2 + f(b))
    return round(integral, 2)
    

