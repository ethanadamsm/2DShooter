import sys, pygame, character, logic

class Player(character.Character):

	def getAccelerating(self):
		self.ablocks = []
		for block in self.blocks:
			if logic.Logic().getCollision(self.x, self.y + self.h, self.w, 2, block.getX(), block.getY(), 20, 20):
				self.ablocks.append(block)
		for block in self.ablocks:
			if block.getType() != "0":
				return False
		return True

	def update(self, map1, l, r, space):
		oldy = self.y
		self.y += self.vy
		self.blocks = map1.getBlocks()
		self.colblocks = []
		for block in self.blocks:
			if logic.Logic().getCollision(self.x, self.y, self.w, self.h, block.getX(), block.getY(), 20, 20):
				if block.getType() != "0":
					self.colblocks.append(block)
		if len(self.colblocks) > 0:
			self.y = oldy
			self.vy = 0
		oldx = self.x
		if l:
			self.x -= 1
		if r:
			self.x += 1
		self.colblocks = []
		for block in self.blocks:
			if logic.Logic().getCollision(self.x, self.y, self.w, self.h, block.getX(), block.getY(), 20, 20):
				if block.getType() != "0":
					if block.getY() < self.y + self.h:
						print block
						self.colblocks.append(block)
		if len(self.colblocks) > 0:
			self.x = oldx 
		if self.getAccelerating():
			self.vy += self.a
		else:
			self.vy = 0
		if self.x + self.w > 600:
			self.x = 600 - self.w
		if self.x < 0:
			self.x = 0
		if self.y < 0:
			self.y = 0
			self.vy = 0

	def jump(self):
		self.vy = -3 
	