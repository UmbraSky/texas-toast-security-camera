import pygame, os
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

os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()


info = pygame.display.Info()
screen_width, screen_height = info.current_w,info.current_h

# Set the width and height of the screen [width, height]
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# the equivalent of the order of execution being within the while 
# true loop
recording = True
# a variable to have the stuff before Brie's loop only fire once
firstRun = True
# -------- Main Program Loop -----------


while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # -- clear the screen
    screen.fill(RED)
 
    # -- put stuff on screen

    # the camera footage
    if firstRun == True:
        result, firstRun, cap,  face_cascade,  body_cascade,  detection,  detection_stopped_time, timer_started,  SECONDS_TO_RECORD_AFTER_DETECTION,  frame_size, fourcc, out = briesStuff(recording, firstRun)
    else:
        result, firstRun, cap,  face_cascade,  body_cascade,  detection,  detection_stopped_time, timer_started,  SECONDS_TO_RECORD_AFTER_DETECTION,  frame_size, fourcc, out = briesStuff(recording, firstRun, cap,  face_cascade,  body_cascade,  detection,  detection_stopped_time, timer_started,  SECONDS_TO_RECORD_AFTER_DETECTION,  frame_size, fourcc, out)
    screen.blit(result, (100,0))

 
    # -- update the screen
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()