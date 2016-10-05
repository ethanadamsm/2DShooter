import sys, pygame, character

class Player(character.Character):
	def update(self):
		self.x += self.vx
		self.y += self.vy