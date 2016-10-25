import sys, pygame

class Item(object):
	def __init__(self, x, y, w, h, image, typee):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.image = image
		self.typee = typee

	def getImage(self):
		return self.image

	def getW(self):
		return self.w

	def getH(self):
		return self.h

	def getType(self):
		return self.typee