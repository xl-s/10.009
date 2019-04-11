# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 20:03:26 2019

@author: Xu Liang

2016 Final Paper
"""

from libdw.sm import SM # For Question 4 and Question 7

# Question 3: maxOccurrences
def maxOccurrences(inp):
	nums = [int(num) for num in inp.split()]
	counts = {}
	for num in nums:
		try:
			counts[num] += 1
		except:
			counts[num] = 1
	mx = 0
	maxlist = []
	for k, v in counts.items():
		if v > mx:
			maxlist = [k]
			mx = v
		elif v == mx:
			maxlist.append(k)
	return sorted(maxlist), mx


# Question 4: RingCounter
class RingCounter(SM):
	start_state = 0

	def get_next_values(self, state, inp):
		if inp or state == 7:
			return 0, '000'
		return state + 1, '{:>3}'.format(str(bin(state + 1)[2:])).replace(' ', '0')


# Question 5: Digital World Warrior and Question 8: getSearchMap
class Avatar:
	
	def __init__(self, name, hp=100, position=(1, 1)):
		self.name = name
		self.hp = hp
		self.position = position

	def getName(self):
		return self._name

	def setName(self, name):
		self._name = name

	def getHP(self):
		return self._hp

	def setHP(self, hp):
		self._hp = hp

	def getPosition(self):
		return self._position

	def setPosition(self, position):
		self._position = position

	name = property(getName, setName)
	hp = property(getHP, setHP)
	position = property(getPosition, setPosition)

	def heal(self, hp=1):
		if hp > 0:
			self.hp += hp

	def attacked(self, hp=-1):
		if hp < 0:
			self.hp += hp

class Map:
	
	def __init__(self, world):
		self.world = world

	def whatIsAt(self, pos):
		if pos in self.world.keys():
			val = self.world[pos]
			if val == 'x':
				return 'Exit'
			elif val > 0:
				return 'Food'
			elif val < 0:
				return 'Enemy'
			elif val == 0:
				return 'Wall'
		return 'Empty'

	def getEnemyAttack(self, pos):
		if self.whatIsAt(pos) == 'Enemy':
			return self.world[pos]
		return False

	def getFoodEnergy(self, pos):
		if self.whatIsAt(pos) == 'Food':
			return self.world[pos]
		return False

	def removeEnemy(self, pos):
		if self.whatIsAt(pos) == 'Enemy':
			del self.world[pos]
			return True
		return False

	def eatFood(self, pos):
		if self.whatIsAt(pos) == 'Food':
			del self.world[pos]
			return True
		return False

	def getExitPosition(self):
		if 'x' in self.world.values():
			for k, v in self.world.items():
				if v == 'x':
					return k
		return None

	def getSearchMap(self):
		# Top 0
		# Right 1
		# Bottom 2
		# Left 3

		# Offset: maximum food value
		# Empty space cost = offset
		# Wall cost = 1000
		# Food cost = offset - food (means that food w max heal has 0 cost)
		# Enemy cost = offset + attack

		def getCost(pos):
			Object = self.whatIsAt(pos)
			if Object == 'Wall':
				return -1000
			elif Object == 'Enemy':
				return self.getEnemyAttack(pos)
			elif Object == 'Food':
				return self.getFoodEnergy(pos)
			else:
				return 0

		world = self.world
		coords = list(world.keys())
		xs = [coord[0] for coord in coords]
		ys = [coord[1] for coord in coords]
		leftlimit = (min(xs), min(ys))
		rightlimit = (max(xs), max(ys))

		costs = {}
		coords = []
		for i in range(leftlimit[0], rightlimit[0]+1):
			for j in range(leftlimit[1], rightlimit[1]+1):
				costs[(i, j)] = getCost((i, j))
				coords.append((i, j))
		offset = max(costs.values())
		costs = {k:(offset - cost) for k, cost in costs.items()}

		search = {}
		for coord in coords:
			search[coord] = {}
			if (coord[0], coord[1]-1) in costs.keys():
				search[coord][0] = ((coord[0], coord[1]-1), costs[(coord[0], coord[1]-1)])
			if (coord[0] + 1, coord[1]) in costs.keys():
				search[coord][1] = ((coord[0]+1, coord[1]), costs[(coord[0]+1, coord[1])])
			if (coord[0], coord[1]+1) in costs.keys():
				search[coord][2] = ((coord[0], coord[1]+1), costs[(coord[0], coord[1]+1)])
			if (coord[0] - 1, coord[1]) in costs.keys():
				search[coord][3] = ((coord[0]-1, coord[1]), costs[(coord[0]-1, coord[1])])
		return search



# Question 7: DW2Game
class DW2Game(SM):
	
	def __init__(self, avatar, world):
		self.start_state = (avatar, world)

	def get_next_values(self, state, inp):
		# inp: (mode, direction)
		# mode can be 'move' or 'attack'. 
		# direction can be 'up', 'down', 'left', 'right'.
		# state: (avatar, map)
		# avatar: name, hp, position (x, y)
		mode, direction = inp
		newAvatar, newMap = state

		if direction == 'up':
			newPos = (newAvatar.position[0], newAvatar.position[1] - 1)
		elif direction == 'down':
			newPos = (newAvatar.position[0], newAvatar.position[1] + 1)
		elif direction == 'right':
			newPos = (newAvatar.position[0] + 1, newAvatar.position[1])
		elif direction == 'left':
			newPos = (newAvatar.position[0] - 1, newAvatar.position[1])
		
		Object = newMap.whatIsAt(newPos)

		if mode == 'move':
			if Object == 'Wall':
				pass
			elif Object == 'Enemy':
				newAvatar.attacked(newMap.getEnemyAttack(newPos))
			elif Object == 'Food':
				newAvatar.position = newPos
				newAvatar.heal(newMap.getFoodEnergy(newPos))
				newMap.eatFood(newPos)
			else:
				newAvatar.position = newPos
		elif mode == 'attack':
			if Object == 'Enemy':
				newMap.removeEnemy(newPos)

		return (newAvatar, newMap), (newAvatar.name, newAvatar.position, newAvatar.hp)

	def done(self, state):
		return True if state[0].position == state[1].getExitPosition() else False

# Missing Question 9 because I'm lazy