# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 11:44:50 2019

@author: Xu Liang

Week 8 Problem Set
"""

# Cohort Sessions 1
class Coordinate:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def magnitude(self):
        return (self.x**2 + self.y**2)**0.5
    
    def translate(self, dx, dy):
        self.x += dx
        self.y += dy
        
    def __eq__(self, other):
        return True if other.x == self.x and other.y == self.y else False
    

# Cohort Sessions 2
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature
        
    def to_fahrenheit(self):
        return self._temperature * 9/5 + 32

    def get_temperature(self):
        return self._temperature
    
    def set_temperature(self, value):
        if value > -273:
            self._temperature = value
        else:
            self._temperature = -273
    
    temperature = property(get_temperature, set_temperature)


# Cohort Sessions 3
from time import time    

class StopWatch:
    def __init__(self):
        self.start_time = time()
        self.end_time = -1
        
    def start(self):
        self.start_time = time()
        
    def stop(self):
        self.end_time = time()
        
    def elapsed_time(self):
        return round(self.end_time - self.start_time, 1) if self.end_time - self.start_time > 0 else None
    

# Cohort Sessions 4
class Line:
    def __init__(self, c0, c1):
        self.c0 = c0
        self.c1 = c1
        
    def __call__(self, x):
        return self.c0 + self.c1 * x
    
    def table(self, L, R, n):
        if L > R or n <= 0:
            return 'Error in printing table'
        step = (R - L)/(n-1)
        if R == L:
            n = 1
        vals = [i*step+L for i in range(n)]
        string = ''
        for val in vals:
            string += '{:10.2f}{:10.2f}\n'.format(round(val, 2), round(self.__call__(val), 2))
        return string
    

# Homework 1
class Time:
    def __init__(self, h, m, s):
        self._hours = h
        self._minutes = m
        self._seconds = s
        
    def __str__(self):
        return 'Time: {}:{}:{}'.format(self._hours, self._minutes, self._seconds)
    
    def getET(self):
        return 60 * 60 * self._hours + 60 * self._minutes + self._seconds
    
    def setET(self, secs):
        secs = secs%86400
        self._hours = secs//3600
        self._minutes = (secs % 3600)//60
        self._seconds = secs % 60
    
    elapsed_time = property(getET, setET)
    

# Homework 2
class Account:
    def __init__(self, owner, account_number, amount):
        self._owner = owner
        self._account_number = account_number
        self._balance = amount
        
    def __str__(self):
        return '{}, {}, balance: {}'.format(self._owner, self._account_number, self._balance)
    
    def deposit(self, amount):
        self._balance += amount
        
    def withdraw(self, amount):
        self._balance -= amount
        

# Homework 3
class Diff:
    def __init__(self, fn, h=1e-4):
        self._fn = fn
        self._h = h
    
    def __call__(self, x):
        return (self._fn(x + self._h) - self._fn(x)) / self._h


# Homework 4
class Polynomial:
    def __init__(self, coef):
        self.coeff = coef
        
    def __add__(self, other):
        if len(self.coeff) > len(other.coeff):
            return Polynomial([s + o for s, o in zip(self.coeff, other.coeff)] + self.coeff[len(other.coeff):])
        elif len(self.coeff) < len(other.coeff):
            return Polynomial([s + o for s, o in zip(self.coeff, other.coeff)] + other.coeff[len(self.coeff):])
        else:
            return Polynomial([s + o for s, o in zip(self.coeff, other.coeff)])
    
    def __sub__(self, other):
        if len(self.coeff) > len(other.coeff):
            return Polynomial([s - o for s, o in zip(self.coeff, other.coeff)] + self.coeff[len(other.coeff):])
        elif len(self.coeff) < len(other.coeff):
            return Polynomial([s - o for s, o in zip(self.coeff, other.coeff)] + [-x for x in other.coeff[len(self.coeff):]])
        else:
            return Polynomial([s - o for s, o in zip(self.coeff, other.coeff)])
        
    def __call__(self, x):
        return sum([c*x**i for i, c in enumerate(self.coeff)])
    
    def __mul__(self, other):
        coef = [0 for x in range(len(other.coeff) + len(self.coeff) - 1)]
        for i, val1 in enumerate(self.coeff):
            for j, val2 in enumerate(other.coeff):
                coef[i+j] += val1 * val2
        return Polynomial(coef)
    
    def differentiate(self):
        self.coeff = [i * x for i, x in enumerate(self.coeff)][1:]
        
    def derivative(self):
        return Polynomial([i * x for i, x in enumerate(self.coeff)][1:])
    
    
# Exercise 1
from math import exp, sin        

class F:
    def __init__(self, a, w):
        self.a = a
        self.w = w
        
    def __call__(self, x):
        return exp(-self.a * x) * sin(self.w * x)
    

# Exercise 2
class Line0:
    def __init__(self, p1, p2):
        self.m = (p2[1] - p1[1]) / (p2[0] - p1[0])
        self.c = p1[1] - p1[0] * self.m
        
    def __call__(self, x):
        return self.c + self.m * x