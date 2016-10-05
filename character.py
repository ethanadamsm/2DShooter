import sys, pygame

class Character(object):
	def __init__(self, x, y, w, h, image):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.vx = 0
		self.vy = 0
		self.image = image

	def render(self, screen):
		screen.blit(self.image, (self.x, self.y))

	def getX(self):
		return self.x
	
	def getVelX(self):
		return self.vx

	def getY(self):
		return self.y

	def getVelY(self):
		return self.vy

	def getW(self):
		return self.w

	def getH(self):
		return self.h

	def getImage(self):
		return self.image

	def setX(self, x):
		self.x = x

	def setVelX(self, vx):
		self.vx = vx

	def setY(self, y):
		self.y = y

	def setVelY(self, vy):
		self.vy = vy

	def setW(self, w):
		self.w = w

	def setH(self, h):
		self.h = h

	def setImage(self, image):
		self.image = image
