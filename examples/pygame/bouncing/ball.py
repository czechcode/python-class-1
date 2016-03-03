import sys, pygame
pygame.init()

size = width, height = 1024, 768
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.gif")
ballrect = ball.get_rect()
clock = pygame.time.Clock()
fps = 120
 
while 1:
	for event in pygame.event.get():
	    if event.type == pygame.QUIT: sys.exit()

	ballrect = ballrect.move(speed)
	if ballrect.left < 0 or ballrect.right > width:
	    speed[0] = -speed[0]
	if ballrect.top < 0 or ballrect.bottom > height:
	    speed[1] = -speed[1]

	screen.fill(black)
	screen.blit(ball, ballrect)
	pygame.display.flip()
	clock.tick(fps)
 