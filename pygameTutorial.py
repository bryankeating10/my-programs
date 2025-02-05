import pygame as pg

pg.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
run = True

player = pg.Rect((300,250,50,50))

while run:

	screen.fill((0,0,0))
	pg.draw.rect(screen, (255,0,0), player)
	key = pg.key.get_pressed()

	if key[pg.K_a] == True:
		player.move_ip(-1,0)
	elif key[pg.K_d] == True:
		player.move_ip(1,0)
	elif key[pg.K_w] == True:
		player.move_ip(0,-1)
	elif key[pg.K_s] == True:
		player.move_ip(0,1)
	for event in pg.event.get():
		print(event)
		if event.type == pg.QUIT:
			run = False
		if event.type == pg.KEYDOWN:
			print("Key has been pressed")
		if event.type == pg.KEYUP:
			print("Key has been released")
		if event.type == pg.MOUSEMOTION:
			print("Mouse is moving")

	pg.display.update()

pg.quit()

