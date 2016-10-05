import sys, pygame, gamemap, player
pygame.init()
pygame.display.set_caption('2D Shooter')

size = width, height, = 600, 400
black = 0, 0, 0
screen = pygame.display.set_mode(size)
map1 = gamemap.GameMap("maps/map1.txt")
player = player.Player(200, 200, 20, 50, pygame.image.load("player.png")) 
player.setVelX(1)

def render():
	screen.fill(black)
	map1.render(screen)
	player.render(screen)
	pygame.display.flip()

def update():
	player.update()

while True:
	render()
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_e:
				print("e")
		if event.type == pygame.KEYUP:
			print ("up")
	update()