import sys, pygame, character, logic

class Player(character.Character):

	def getAccelerating(self):
		for colblock in self.colblocks:
			if colblock.getType() != "0":
				return False
		return True

	def clamp(self, l, r, space):
		fl = ""
		fr = ""
		ft = ""
		fb = ""
		left = []
		right = []
		top = []
		bottom = []
		for block in self.colblocks:
			if block.getX() < self.x:
				left.append(block)
			if block.getX() > self.x + 20:
				right.append(block)
			if block.getY() < self.y:
				top.append(block)
			if block.getY() > self.y + 50:
				bottom.append(block)
		if len(self.colblocks) > 0:
			fl = self.colblocks[0].getX()
			fr = self.colblocks[0].getX()
			ft = self.colblocks[0].getY()
			fb = self.colblocks[0].getY()
		for block in self.colblocks:
			if block.getX() > fl:
				fl = block.getX()
			if block.getX() < fr:
				fr = block.getX()
			if block.getY() < ft:
				ft = block.getY()
			if block.getY() > fb:
				fb = block.getY()
		if fl != "":
			print fl
			if self.x < fl + 20 and self.y + 40 > ft + 3 and l:
				self.x = fl
				self.vx = 0
				print " fasdf"
			elif self.x + 20 > fr and self.y + 40 > ft + 3 and r:
				self.x = fr
				self.vx = 0
			if self.y < fb:
				self.y = fb - 39
				self.vy = 0

	def update(self, map1, l, r, space):
		blocks = map1.getBlocks()
		self.colblocks = []
		for block in blocks:
			if logic.Logic().getCollision(self.x, self.y, self.w, self.h, block.getX(), block.getY(), 20, 20):
				if block.getType() != "0":
					self.colblocks.append(block)
		if self.getAccelerating():
			self.vy += self.a
		else:
			self.vy = 0
		self.clamp(l, r, space)
		if l:
			self.x -= 1
		if r:
			self.x += 1
		self.y += self.vy

	def jump(self):
		self.y -= 20
		self.vy = -3 
	