# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 15:35:34 2019

@author: Xu Liang

Week 2 Problem Set
"""

import math # For Homework 3

g = 9.81 # Gravitational constant, for Cohort Sessions 1

# Coordinate class, for Cohort Sessions 3 and Cohort Sessions 7
class Coordinate():
    x = 0.0
    y = 0.0


# Cohort Sessions 1
def position_velocity(v0, t):
    y = v0 * t - 0.5 * g * t * t # y(t)
    ydot = v0 - g * t # y'(t)
    return round(y, 2), round(ydot, 2)


# Cohort Sessions 2
def bmi(weight, height):
    BMI = weight / ((height/100)**2) # BMI
    return round(BMI, 1)


# Cohort Sessions 3
def area_of_triangle(p1, p2, p3):
    side1 = length(p1, p2)
    side2 = length(p2, p3)
    side3 = length(p3, p1)
    s = 0.5 * (side1 + side2 + side3)
    area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5
    return round(area, 2)
    
def length(p1, p2):
    dy = p2.y - p1.y
    dx = p2.x - p1.x
    distance = (dy ** 2 + dx ** 2) ** 0.5
    return distance


# Cohort Sessions 5
def describe_bmi(BMI):
    if(BMI >= 27.5):
        return "high risk"
    elif(BMI >= 23.0):
        return "moderate risk"
    elif(BMI >= 18.5):
        return "low risk"
    else:
        return "nutritional deficiency"


# Cohort Sessions 6
def letter_grade(mark):
    if(mark > 100 or mark < 0):
        return None
    
    if(mark >= 90):
        return 'A'
    elif(mark >= 80):
        return 'B'
    elif(mark >= 70):
        return 'C'
    elif(mark >= 60):
        return 'D'
    else:
        return 'E'
    

# Cohort Sessions 7
def is_in_square(centre1, side1, centre2, side2):
    xseparation = abs(centre1.x - centre2.x)
    yseparation = abs(centre1.y - centre2.y)
    mindistance = side1 / 2 + side2 / 2
    
    if(xseparation > mindistance or yseparation > mindistance):
        return False
    else:
        return True
    


# Homework 1
def fahrenheit_to_celsius(f):  
    c = (f - 32) * 5/9
    return round(c, 2)
    

# Homework 2
def celsius_to_fahrenheit(c):
    f = c * 9/5 + 32
    return round(f, 2)


# Homework 3
def area_vol_cylinder(radius, length):
    area = radius * radius * math.pi
    volume = area * length
    return round(area, 2), round(volume, 2)


# Homework 4
def wind_chill_temp(t_a, v):
    t_wc = 35.74 + 0.6215 * t_a - 35.75 * (v ** 0.16) + 0.4275 * t_a * (v ** 0.16)
    return t_wc


# Homework 5
def minutes_to_years_days(minutes):
    totaldays = minutes / (24 * 60)
    years = totaldays // 365
    days = totaldays % 365
    return years, round(days, 1)


# Homework 6
def investment_val(investment, interest, years):
    futureval = investment * ((1 + interest/12/100) ** (years*12))
    return round(futureval, 2)


# Homework 7
def is_larger(n1, n2):
    if(n1 > n2):
        return True
    else:
        return False
    

# Homework 8
def check_value(n1, n2, n3, x):
    if(x > n1 and x > n2 and x < n3):
        return True
    else:
        return False

