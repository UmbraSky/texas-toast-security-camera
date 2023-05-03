import pygame
from bries_work import briesStuff
 
# Define some colors
DARKEST = (26, 17, 16)
DARKERGRAY = (127, 115, 115)
LIGHTERGRAY = (182, 192, 189)
OFFWHITE = (236, 225, 224)
PINK = (255, 209, 223)
SALMON = (202, 63, 66)
ORANGEYRED = (233, 41, 33)
RED = (255, 0, 21)
MAROON = (132, 14, 1)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# keeps track of if brie's stuff should still be accumulating frames
recording = False
# -------- Main Program Loop -----------


while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(RED)
 
    # --- Drawing code should go here
    result = briesStuff()
    screen.blit(result, (0,0))
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()