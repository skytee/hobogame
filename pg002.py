#!/usr/bin/python
import pygame
from pygame.locals import *
pygame.init()
pygame.font.init()

size = width, height = 640, 400
speed = [2, 2]
black = 0, 0, 0
map_position = 0
map_direction = 0
hobo_move = 0
fg_speed = 3
bg_speed = 1


screen = pygame.display.set_mode(size) # create instance of: surface

ground = []
mountain = []
ground.append(pygame.image.load("img/ground-grass.bmp").convert())
ground.append(pygame.image.load("img/ground-grass2stone.bmp").convert())
ground.append(pygame.image.load("img/ground-stone.bmp").convert())
ground.append(pygame.image.load("img/ground-stone2bridge.bmp").convert())
ground.append(pygame.image.load("img/ground-bridge1.bmp").convert())
ground.append(pygame.image.load("img/ground-bridge2.bmp").convert())
ground.append(pygame.image.load("img/ground-bridge-pillar.bmp").convert())
ground.append(pygame.image.load("img/ground-bridge2stone.bmp").convert())
ground.append(pygame.image.load("img/ground-dirt2stone.bmp").convert())
ground.append(pygame.image.load("img/ground-grass2stone.bmp").convert())
ground.append(pygame.image.load("img/ground-stone2bridge.bmp").convert())
ground.append(pygame.image.load("img/ground-stone2dirt.bmp").convert())
ground.append(pygame.image.load("img/ground-dirt.bmp").convert())
ground.append(pygame.image.load("img/ground-dirt2stone.bmp").convert())
ground.append(pygame.image.load("img/ground-stone2grass.bmp").convert())
mountain.append(pygame.image.load("img/mountain-flat.bmp").convert())
mountain.append(pygame.image.load("img/mountainglacier.bmp").convert())
mountain.append(pygame.image.load("img/mountain-kermit.bmp").convert())
mountain.append(pygame.image.load("img/mountain-m.bmp").convert())

hoboimg = pygame.image.load("img/hobo.png").convert()

bg_order = [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1 ];
ground_order = [ 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 3, 4, 5, 6, 4, 5, 6, 4, 5, 7, 2, 2, 2, 2, 2, 2, 2, 2, 11, 12, 12, 12, 12, 12, 12, 12, 12, 12, 13, 2, 2, 2, 2, 14, 0, 0, 0]

# set transparency
transColor = hoboimg.get_at((0,0))
hoboimg.set_colorkey(transColor)
screen.set_colorkey(transColor)

hobo = []
for i in range (0, 14):
	cropped = pygame.Surface((28, 48))
	cropped.blit(hoboimg, (0,0), ((28*i), 0, 28, 48))
	cropped.set_colorkey(transColor)
	hobo.append(cropped)


screen.fill(black)

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		elif event.type == KEYDOWN and event.key == K_RIGHT:
			map_direction = +1
			hobo_move = 1
		elif event.type == KEYDOWN and event.key == K_LEFT:
			map_direction = -1
			hobo_move = 1
		elif event.type == KEYUP:
			hobo_move = 0
	
	# blit background tiles (3 fully and 2 partially visible)
	for i in range (0, 5):
		bg_pos = map_position * bg_speed; # determine bg position
		scroll_pos = bg_pos % 160 # account for tile width 
		scroll_pos *= -1 # deduct part of img out of screen
		scroll_pos += (i*160) # account for tiles blitted
		img_num = bg_order[i+(bg_pos/160)] # select tile to blit
		screen.blit(mountain[img_num], (scroll_pos, 0))

	# blit ground tiles (10 fully and 2 partially visible)
	for i in range (0, 11):
		fg_pos = map_position * fg_speed;
		scroll_pos = fg_pos % 64 
		scroll_pos *= -1
		scroll_pos += (i*64) 
		#screen.blit(ground[0], (scroll_pos, 288))
		i %= len(ground_order)
		j = i+(fg_pos/64)
		img_num = ground_order[i+(fg_pos/64)] # select tile to blit
		screen.blit(ground[img_num], (scroll_pos, 288))

	# blit hobo
	if hobo_move == 0:
		if map_direction >= 0 :
			screen.blit(hobo[6], (200, 240) )
		else:
			screen.blit(hobo[7], (200, 240) )
	else:
		fg_pos = map_position/4;
		i = fg_pos % 6
		if map_direction == 1:
			screen.blit(hobo[i], (200, 240) )
		else:
			screen.blit(hobo[13-i], (200, 240) )
	

#	ballrect = ballrect.move(speed);
#	if ballrect.left < 0 or ballrect.right > width:
#		speed[0] = -speed[0]
#	if ballrect.top < 0 or ballrect.bottom > height:
#		speed[1] = - speed[1]
#
#	screen.blit(background, (0, 0))
#	screen.blit(ball, ballrect)

	# update display, wait for frame and move forward
	pygame.display.flip()
	pygame.time.delay(33)
	if hobo_move == 1:
		map_position += map_direction

