import sys, pygame

class Block(object):
	def __init__(self, x, y, typee, image):
		self.x = x
		self.y = y
		self.typee = typee
		self.image = image

	def render(self, screen):
		screen.blit(self.image, (self.x, self.y))