# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 19:39:57 2019

@author: Xu Liang

2017 Final Paper
"""

from libdw.sm import SM

# Question 3: complete_ISBN
def complete_ISBN(inp):
	count = 1
	total = 0
	for char in inp:
		total += count * int(char)
		count += 1
	checksum = total % 11
	return inp+'X' if checksum == 10 else inp+str(checksum)


# Question 4: get_products
def get_products(inlist, test):
	d = {}
	for elm in inlist:
		prod = 1
		for num in elm:
			prod *= num
		d.setdefault(prod, []).append(elm)
	if test in d.keys():
		ret2 = d[test]
	else:
		ret2 = None
	return d, ret2


# Question 5: SpellCheckSM
class SpellCheckSM(SM):

	first = 'kgstdnhbmr'
	second = 'aeiou'

	def __init__(self):
		self.start_state = 'new word'

	def get_next_values(self, state, inp):
		if state == 'new word':
			if inp == ' ':
				return 'new word', ''
			elif inp in self.first:
				return 'consonant', ''
			else:
				return 'error', ''
		elif state == 'consonant':
			if inp == ' ':
				return 'new word', 'error'
			elif inp in self.second:
				return 'vowel', ''
			else:
				return 'error', ''
		elif state == 'vowel':
			if inp == ' ':
				return 'new word', 'ok'
			else:
				return 'error', ''
		elif state == 'error':
			if inp == ' ':
				return 'new word', 'error'
			else:
				return 'error', ''


# Question 6: Parallelogram
class Parallelogram:

	def __init__(self, side1, side2, diagonal):
		self.side1 = side1
		self.side2 = side2
		self.diagonal = diagonal

	def __str__(self):
		return '{:.2f}'.format(self.diagonal)

	def getD(self):
		return self._diagonal

	def setD(self, val):
		if val >= 0:
			self._diagonal = val
		else:
			self._diagonal = 0

	def __call__(self):
		return True if self.side1 + self.side2 > self.diagonal else False

	def calc_area(self):
		s = (self.side1 + self.side2 + self.diagonal)/2
		return round(2 * (s * (s-self.side1) * (s - self.side2) * (s - self.diagonal))**0.5, 2)

	diagonal = property(getD, setD)

class Rhombus(Parallelogram):
	
	def __call__(self):
		return True if self.side1 == self.side2 else False

class Rectangle(Parallelogram):
	
	def __call__(self):
		return True if self.side1**2 + self.side2**2 == self.diagonal**2 else False

class Square(Rectangle):
	
	def __call__(self):
		return True if (self.side1 == self.side2) and (self.side1**2 + self.side2**2 == round(self.diagonal**2, 5)) else False


# Question 7: procrastination
def procrastination(assignments):
	# Sort by deadline.
	assignments = sorted(assignments, key=lambda x: x.deadline, reverse=True)
	earliest = assignments[0].deadline
	for a in assignments:
		if earliest < a.deadline:
			earliest -= a.duration
		else:
			earliest = a.deadline - a.duration
	return earliest if earliest > 0 else -1

class MyTask(object):

	def __init__(self, deadline, duration):
		self.deadline = deadline
		self.duration = duration

	def __str__(self):
		return 'T(%d,%d)' % (self.deadline, self.duration)

