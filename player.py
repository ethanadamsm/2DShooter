import sys, pygame, character, logic

class Player(character.Character):

	def getAccelerating(self):
		for colblock in self.colblocks:
			if colblock.getType() != "0":
				return False
		return True

	def clamp(self):
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
			self.x = fl + 5
			if self.x < fl and self.vx < 0:
				self.x = fl + 20
				self.vx = 0
				print self.x + " fasdf"

	def update(self, map1):
		blocks = map1.getBlocks()
		self.colblocks = []
		for block in blocks:
			if logic.Logic().getCollision(self.x, self.y, self.w, self.h, block.getX(), block.getY(), 20, 20):
				if block.getType() != "0":
					self.colblocks.append(block)
		self.clamp()
		if self.getAccelerating():
			self.vy += self.a
		else:
			self.vy = 0
		self.x += self.vx
		self.y += self.vy

	def jump(self):
		self.y -= 20
		self.vy = -3
	