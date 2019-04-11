# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 20:44:32 2019

@author: Xu Liang

2018 Final Paper
"""

from libdw.sm import SM # For Question 6

# Question 3: equity
def equity(f):
	return (sum([elm[0] for elm in f.values()]), \
		sum([elm[1] for elm in f.values()]), \
		sum([elm[0] - elm[1] for elm in f.values()]))


# Question 4: wordcounts
def wordcount(s):
	for char in ':;,.-':
		s = s.replace(char, '')
	lines = [line.strip().split() for line in s.split('\n')]
	counts = []
	for line in lines:
		count = 0
		for i, word in enumerate(line):
			line[i] = ''
			if word not in line:
				count += 1
		if not count: count = None
		counts.append(count)
	return counts


# Question 5: Person
class Person:

	def __init__(self, name='Unknown', age=0, contact_details={'phone':'+65 0000 0000', 'email':'nobody@nowhere.com.sg'}, mother=None):
		self.name = name
		self.age = age
		self.contact_details = contact_details
		self.mother = mother

	def getName(self):
		return self._name

	def setName(self, val):
		if type(val) == str and len(val): self._name = val

	def getAge(self):
		return self._age

	def setAge(self, val):
		if type(val) == int and val >= 0: self._age = val

	def getEmail(self):
		return self.contact_details['email']

	def setEmail(self, val):
		valid = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ._'
		if type(val) == str:
			if val.count('@') == 1:
				email = val.split('@')
				for char in email[0]:
					if char not in valid:
						return None
				if '.' in email[1]: self.contact_details['email'] = val

	def getMother(self):
		return self._mother

	def selfAncestor(self, person):
		current = person
		while(current.mother):
			if current.mother is self:
				return True
			current = current.mother
		return False

	def setMother(self, val):
		if val == None:
			self._mother = val
		if type(val) == Person and not val is self and not self.selfAncestor(val):
			self._mother = val

	name = property(getName, setName)
	age = property(getAge, setAge)
	email = property(getEmail, setEmail)
	mother = property(getMother, setMother)


# Question 6: VacuumRobot
class VacuumRobot(SM):
	
	def __init__(self):
		self.start_state = {'coords':(0, 0), 'visited':[(0, 0)], 'facing':(0, 1)}

	def get_next_values(self, state, inp):
		oldCoords = state['coords']
		newPos = (state['coords'][0] + state['facing'][0], state['coords'][1] + state['facing'][1])
		if not state:
			return 0, 'STOP'
		if inp or newPos in state['visited']:
			newDir = (-1 * state['facing'][1], state['facing'][0])
			newPos = (newDir[0] + state['coords'][0], newDir[1] + state['coords'][1])
			if newPos in state['visited']:
				#end
				return 0, oldCoords
			else:
				newState = state
				newState['coords'] = newPos
				newState['visited'].append(state['coords'])
				newState['facing'] = newDir
				return newState, oldCoords
		else:
			newState = state
			newState['coords'] = newPos
			newState['visited'].append(state['coords'])
			return newState, oldCoords


# Question 7: SMExtra
class SMExtra(SM):

	# valid_inputs: list of all possible inputs
	# assume can use start state too

	def get_input_for_output(self, output_list):
		state = start_state
		in_list = []
		for out in output_list:
			for inp in valid_inputs:
				s, o = self.get_next_values(state, inp)
				if o == out:
					in_list.append(inp)
					state = s
					break
		return in_list

