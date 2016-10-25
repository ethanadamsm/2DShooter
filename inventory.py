import sys, pygame

class Inventory(object):
	def __init__(self):
		self.itemList = []
		self.image = pygame.image.load("inventory.png")
		self.font = pygame.font.SysFont("comicsansms", 30)
		self.current = 0
		self.invensel = pygame.image.load("inventorysel.png")
		self.visible = True

	def addItem(self, item):
		self.itemList.append(item)

	def render(self, screen):
		#self.itemList[self.current].render(screen)
		if self.visible:
			screen.blit(self.image, (10, 330))
			x = 20
			y = 340
			num = 1
			for item in self.itemList:
				scalex = 50 / item.getW()
				scaley = 50 / item.getH()
				cur = pygame.transform.scale(item.getImage(), (scalex, scaley))
				screen.blit(item.getImage(), (x, y))
				text = self.font.render(str(num), True, (0, 0, 0))
				screen.blit(text, (x, 290))
				x += 50
				num += 1
			screen.blit(self.invensel, ((self.current * 50) + 10, 332))

	def update(self):
		for item in self.itemList:
			item.update()
			print(self.itemList[self.current].getVisible())

	def moveItem(self, vx, vy):
		self.itemList[self.current].setVelX(vx)
		self.itemList[self.current].setVelY(vy)

	def setItem(self, x, y):
		if len(self.itemList) > 0:
			self.itemList[self.current].setX(x)
			self.itemList[self.current].setY(y)

	def rotateItem(self, angle):
		self.itemList[self.current].rotateItem(angle)

	def getX(self):
		return self.itemList[self.current].getX()

	def getY(self):
		return self.itemList[self.current].getY()

	def getW(self):
		return self.itemList[self.current].getW()

	def getH(self):
		return self.itemList[self.current].getH()

	def getItem(self, index):
		return self.itemList[index]

	def setCurrent(self, current):
		self.current = current

	def getCurrent(self):
		return self.itemList[self.current]

	def getInventory(self):
		return self.itemList

	def getType(self):
		return self.itemList[self.current].getType()

	def setVisible(self, visible):
		self.visible = visible