import pygame
 
# Start GUI 
pygame.init()
 
# Set the width and height of the screen [width, height]
screen = pygame.display.set_mode((320, 320))

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
while not done:

    # Listen for key's
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
 
    # Fill background with color
    screen.fill((255, 255, 255))
     
    myfont = pygame.font.SysFont(None, 15)
    label = myfont.render("Some text!", True, (0, 0, 0))
    screen.blit(label, (140, 160))

    # Update screen
    pygame.display.flip()
    pygame.display.set_caption("FPS: {0:.2f}".format(clock.get_fps()))
 
    # Set FPS
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
