import pygame
import random

pygame.init()
screen = pygame.display.set_mode((400, 400))
 
bullethole_orig = pygame.image.load("resources/bullethole.png")
bullethole = bullethole_orig
bulletholerect = bullethole.get_rect()

click_sound = pygame.mixer.Sound("resources/gun.ogg")

done = False
while not done:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            randomsize = random.randrange(100, 200)

            bullethole = pygame.transform.scale(bullethole_orig, (randomsize, randomsize))
            bulletholerect = bullethole.get_rect()

            mousepos = pygame.mouse.get_pos()
            bulletholerect.centerx = mousepos[0]
            bulletholerect.centery = mousepos[1]
        
            click_sound.play()

    screen.fill((255, 255, 255)) 
    screen.blit(bullethole, bulletholerect)
    pygame.display.flip()

pygame.quit()
