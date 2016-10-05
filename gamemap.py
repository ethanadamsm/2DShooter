import sys, pygame, block

class GameMap(object):
	def __init__(self, filename):
		data = []
		self.blocks = []
		image1 = pygame.image.load("block1.png")
		image2 = pygame.image.load("block2.png")
		image3 = pygame.image.load("block3.png")
		file = open(filename, 'r')
		for line in file:
			words = line.split()
			for word in words:
				data.append(word)

		x = 0
		y = 0
		for z in range(0, 600):
			if data[z] == "0":
				self.blocks.append(block.Block(x, y, data[z], image1))
			elif data[z] == "1":
				self.blocks.append(block.Block(x, y, data[z], image2))
			elif data[z] == "2":
				self.blocks.append(block.Block(x, y, data[z], image3))
			x += 20
			if x == 600:
				x = 0
				y += 20

	def render(self, screen):
		for i in range(0, 600):
			self.blocks[i].render(screen)

	def update(self, screen):
		print("update")