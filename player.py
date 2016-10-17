import sys, pygame, character, logic

class Player(character.Character):

	def getAccelerating(self):
		for colblock in self.colblocks:
			if colblock.getType() != "0":
				return False
		return True

	def update(self, map1):
		blocks = map1.getBlocks()
		self.colblocks = []
		for block in blocks:
			if logic.Logic().getCollision(self.x, self.y, self.w, self.h, block.getX(), block.getY(), 20, 20):
				self.colblocks.append(block)
		if self.getAccelerating():
			self.vy += self.a
		else:
			self.vy = 0
		self.x += self.vx
		self.y += self.vy

	