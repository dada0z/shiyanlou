#-*- coding:utf-8 -*-
import curses
from random import randrange, choice
from collections import defaultdict

actions = ['Up', 'Left', 'Down', 'Right', 'Restart', 'Exit']
letterCodes = [ord(ch) for ch in 'WASDRQwasdrq']
actionDict = dict(zip(letterCodes, actions*2))

def getUserAction(keyboard):
	ch = 'N'
	while ch not in actionDict:
		ch = keyboard.getch()
	return actionDict[ch]

def transpose(field):
	return [list(row) for row in zip(*field)]

def invert(field):
	return [row[::-1] for row in field]

class GameField(object):
	"""docstring for GameField"""
	def __init__(self, height=4, width=4, win=2048):
		super(GameField, self).__init__()
		self.height = height
		self.width = width
		self.win = win
		self.score = 0
		self.highScore = 0
		self.reset()

	def reset(self):
		if self.score > self.highScore:
			self.highScore = self.score
		self.score = 0
		self.field = [[0 for i in range(self.width)] for j in range(self.height)]
		self.spawn()
		self.spawn()

	def move(self, direction):
		def moveRowLeft(row):
			def tighten(row):
				newRow = [i for i in row if i!=0]
				newRow += [0 for i in range(len(row) - len(newRow))]
				return newRow

			def merge(row):
				pair = False
				newRow = []
				for i in range(len(row)):
					if pair:
						newRow.append(2*row[i])
						self.score += 2*row[i]
						pair = False
					else:
						if i +1 < len(row) and row[i] == row[i+1]:
							pair = True
							newRow.append(0)
						else:
							newRow.append(row[i])
				asssert len(newRow) == len(row)
				return newRow
			return tighten(merge(tighten(row)))
		
		