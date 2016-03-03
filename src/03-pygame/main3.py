import pygame
 
pygame.init()

width = 400
height = 320
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Bouncing")

ball = pygame.image.load("resources/ball.gif")
ballrect = ball.get_rect()

done = False 
while not done:

    # Listen for key's
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True

    ballrect.x = 100

    screen.fill((255, 255, 255))
    screen.blit(ball, ballrect)

    # Update screen
    pygame.display.flip()
 
pygame.quit()
