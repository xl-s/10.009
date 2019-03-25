# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 08:24:32 2019

@author: Xu Liang

Week 9 Problem Set
"""

from libdw.sm import SM

# Cohort Sessions 1
class CM(SM):
    start_state = 0
    coins = [50, 100]
    price = 100
    
    def get_next_values(self, state, inp):
        if inp not in self.coins:
            display = 0
            if state:
                display = 50
            return state, (display, '--', inp)
        if not state:
            if inp < self.price:
                return 1, (inp, '--', 0)
            else:
                return 0, (0, 'coke', self.price - inp)
        else:
            return 0, (0, 'coke', inp - 50)
        

# Cohort Sessions 2            
class SimpleAccount(SM):
    def __init__(self, balance):
        self.start_state = balance
    
    def get_next_values(self, state, inp):
        if state < 100 and inp < 0:
            return state + inp - 5, state + inp - 5
        else:
            return state + inp, state + inp
        

# Homework 1
class CommentsSM(SM):
    start_state = False
    
    def get_next_values(self, state, inp):
        return (True, inp) if ((state and inp != '\n') or inp == '#') else (False, None)

                
#Homework 2
class FirstWordSM(SM):
    start_state = True, False
    
    def get_next_values(self, state, inp):
        if inp == '\n':
                return (True, False), None
        if state[0]:
            if inp == ' ':
                return ((False, False), None) if state[1] else ((True, False), None)
            else:
                return (True, True), inp
        else:
                return (False, False), None
            
