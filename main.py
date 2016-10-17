import sys, pygame, gamemap, player
pygame.init()
pygame.display.set_caption('2D Shooter')

size = width, height, = 600, 400
black = 0, 0, 0
screen = pygame.display.set_mode(size)
map1 = gamemap.GameMap("maps/map1.txt")
player = player.Player(200, 0, 20, 50, pygame.image.load("player.png")) 

def render():
	screen.fill(black)
	map1.render(screen)
	player.render(screen)
	pygame.display.flip()

def update():
	player.update(map1)

while True:
	render()
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				player.setVelX(-1)
			if event.key == pygame.K_d:
				player.setVelX(1)
			if event.key == pygame.K_w:
				player.setVelY(-1)
			if event.key == pygame.K_s:
				player.setVelY(1)
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_a or event.key == pygame.K_d:
				player.setVelX(0)
			if event.key == pygame.K_w or event.key == pygame.K_s:
				player.setVelY(0)
	update()