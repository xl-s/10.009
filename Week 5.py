# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 09:03:14 2019

@author: Xu Liang

Week 5 Problem Set
"""

# Cohort Sessions 1
from random import randint

craps = set([2, 3, 12])
naturals = set([7, 11])

def roll_two_dices():
    return randint(1, 6), randint(1, 6)

def print_lose():
    print('You lose')

def print_win():
    print('You win')

def print_point(p):
    print('Your points are {:d}'.format(p))

def is_craps(n):
    if n in craps:
        return True
    else:
        return False

def is_naturals(n):
    if n in naturals:
        return True
    else:
        return False

def play_craps():
    point = -1
    while True:
        n1, n2 = roll_two_dices()
        sumn = n1 + n2
        print('You rolled {:d} + {:d} = {:d}'.format(n1, n2, sumn))
        if point == -1:
            if is_craps(sumn):
                print_lose()
                return 0
            elif is_naturals(sumn):
                print_win()
                return 1
            point = sumn
            print_point(point)
        else:
            if sumn == 7:
                print_lose()
                return 0
            elif sumn == point:
                print_win()
                return 1
            

# Cohort Sessions 2
def leap_year(year):
    if year // 4 != year/4:
        return False
    elif year // 100 != year/100:
        return True
    elif year // 400 != year/400:
        return False
    else:
        return True

def day_of_week_jan1(year):
    if year < 1800 or year > 2099:
        raise ValueError("Year must be between 1800 and 2099.")
    day = (1 + 5 * ((year - 1) % 4) + 4 * ((year - 1) % 100) + 6 * ((year - 1) % 400)) % 7
    return day

def num_days_in_month(month_num, leap_year):
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month_num < 1 or month_num > 12:
        raise ValueError("Month must be between 1 and 12.")
    if leap_year and month_num == 2:
        return 29
    return days[month_num]

def construct_cal_month(month_num, first_day_of_month, num_days_in_month):
    months = {1: "January", 2: "February", 3: "March", 4: "April", \
              5: "May", 6: "June", 7: "July", 8: "August", \
              9: "September", 10: "October", 11: "November", 12: "December"}
    monthlist = []
    nextday = 0
    # Construct data stucture
    daysInWeek = 7 - first_day_of_month
    while nextday < num_days_in_month:
        weeklist = []
        for day in range(daysInWeek):
            nextday += 1
            weeklist.append(nextday)
        monthlist.append(weeklist)
        if num_days_in_month - nextday < 7:
            daysInWeek = num_days_in_month - nextday
        else:
            daysInWeek = 7
    # Format output
    # Spaces are two before every single digit, or one before every double
    # 21 characters per row total
    outlist = []
    outlist.append(months[month_num])
    for weekno, week in enumerate(monthlist):
        outlist.append('')
        for day in week:
            if(day < 10):
                outlist[weekno + 1] += '  ' + str(day)
            else:
                outlist[weekno + 1] += ' ' + str(day)
        if weekno == 0:
            totalchars = len(outlist[1])
            spacing = (21 - totalchars) * ' '
            outlist[1] = spacing + outlist[1]
    
    return outlist

def construct_cal_year(year):
    yearlist = [year]
    leap = leap_year(year)
    firstday = day_of_week_jan1(year)
    numdays = num_days_in_month(1 ,leap)
    for month in range(1, 13):
        numdays = num_days_in_month(month, leap)
        yearlist.append(construct_cal_month(month, firstday, numdays))
        firstday = (firstday + numdays + 1) % 7 - 1
        if(firstday == -1):
            firstday = 6
    return yearlist

def display_calendar(calendar_year):
    cal = construct_cal_year(calendar_year)
    output = ''
    for i, elm in enumerate(cal[1:], 1):
        if i != 1 :
            output += '\n'
        for ind, subelm in enumerate(elm):
            if ind == 1:
                output += '  S  M  T  W  T  F  S\n'
            output += subelm
            output += '\n'
    output = output[:-1]
    return output

# Cohort Sessions 3
def fact_rec(n):
    return n * fact_rec(n - 1) if n else 1


# Homework 1
def get_data():
    inp = input("Enter integer pair (hit Enter to quit):\n")
    return inp

def extract_values(string):
    values = string.split(' ')
    return int(values[0]), int(values[1])

def calc_ratios(num):
    if num[1]:
        return num[0]/num[1]
    

# Homework 2
def display_calendar_modified(calendar_year, month):
    cal = construct_cal_year(calendar_year)
    output = ''
    
    if month:
        for ind, subelm in enumerate(cal[month]):
            if ind == 1:
                output += '  S  M  T  W  T  F  S\n'
            output += subelm
            output += '\n'
        output = output[:-1]
        return output
    
    for i, elm in enumerate(cal[1:], 1):
        if i != 1 :
            output += '\n'
        for ind, subelm in enumerate(elm):
            if ind == 1:
                output += '  S  M  T  W  T  F  S\n'
            output += subelm
            output += '\n'
    output = output[:-1]
    return output


