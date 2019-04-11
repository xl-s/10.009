# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 14:47:10 2019

@author: Xu Liang

2015 Final Paper
"""

from libdw.sm import SM # For Question 6

# Question 3: compTrace
def compTrace(A):
	return sum([A[i][i] for i in range(len(A))])


# Question 4: findKey
def findKey(dInput, strInput):
	result = []
	for k, v in dInput.items():
		if v == strInput:
			result.append(k)
	return sorted(result)


# Question 5: Square
class Square:

	def __init__(self, x=0, y=0, sideLength=1.0):
		self.x = x
		self.y = y
		self.sideLength = sideLength

	def getCenter(self):
		return (self.x, self.y)

	def getSideLength(self):
		return self.sideLength

	def getArea(self):
		return self.sideLength ** 2

	def getPerimeter(self):
		return self.sideLength * 4

	def containPoint(self, px, py):
		return True if (abs(px - self.x) <= self.sideLength/2) and (abs(py - self.y) <= self.sideLength/2) else False

	def containSquare(self, inSquare):
		maxDisplacement = (self.sideLength - inSquare.sideLength) / 2
		return False if (abs(inSquare.x - self.x) > maxDisplacement) or (abs(inSquare.y - self.y) > maxDisplacement) else True


# Question 6: Elevator
class Elevator(SM):
	start_state = 'First'

	def get_next_values(self, state, inp):
		if state == 'First':
			if inp == 'Down':
				return 'First', 'First'
			elif inp == 'Up':
				return 'Second', 'Second'
		elif state == 'Second':
			if inp == 'Down':
				return 'First', 'First'
			elif inp == 'Up':
				return 'Third', 'Third'
		elif state == 'Third':
			if inp == 'Down':
				return 'Second', 'Second'
			elif inp == 'Up':
				return 'Third', 'Third'


# Question 7: countNumOpenLocker
def countNumOpenLocker(K): # Direct Solution
	lockers = [1 for i in range(K)]
	for i in range(2, K+1):
		for j in list(range(len(lockers)))[(i-1)::i]:
			if lockers[j]:
				lockers[j] = 0
			else: 
				lockers[j] = 1
	return sum(lockers)

from math import sqrt

def countNumOpenLockerEfficient(K): # Efficient Solution
	return int(sqrt(K))

