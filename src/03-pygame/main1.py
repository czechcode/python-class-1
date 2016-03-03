# import PyGame library
import pygame
 
# Define some colors
WHITE = (255, 255, 255)

# Start GUI 
pygame.init()
 
# Set the width and height of the screen [width, height]
screen = pygame.display.set_mode((320, 320))

# Set window title
pygame.display.set_caption("My First Game")
 
# Loop until the user clicks the close button.
done = False

while not done:

    # Listen for key's
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
 
    # Fill background with color
    screen.fill(WHITE)
 
    # Update screen
    pygame.display.flip()
 
# Close the window and quit.
pygame.quit()
