import pygame, os
from bries_work import briesStuff
from buttonCreater import Button
from colors import *
from time import sleep

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

# a timer to stop buttons from pressing multiple times in a press
btnTimer = 0
btnTimerMax = 150

# a list of all buttons
buttons = []

# the equivalent of the order of execution being within the while 
# true loop
recording = True
# a variable to have the stuff before Brie's loop only fire once
firstRun = True

# holds the last frame shown for when the video is paused
lastFrame = None

startAndStopMode = "main"

deactivateAndActivateMode = "main"

camOn = True
#--- button functions ----
def startAndStop():
    global camOn
    global btnTimer
    global startAndStopMode
    if btnTimer == 0:
        if camOn == True:
            camOn = False
            startAndStopBtn.mode = "alt"
            startAndStopMode = "alt"
            print("manually stopped recording...")
        else:
            camOn = True
            startAndStopBtn.mode = "main"
            startAndStopMode = "main"
            print("manually continued recording...")
        btnTimer += 1
    elif btnTimer >= btnTimerMax:
        btnTimer = 0
    else:
        btnTimer += 1

recogOn = True
def deactivateAndActivate():
    global recogOn
    global btnTimer
    global deactivateAndActivateMode
    if btnTimer == 0:
        if recogOn == True:
            recogOn = False
            deactivateAndActivateBtn.mode = "alt"
            deactivateAndActivateMode = "alt"
            print("diactivated intruder recognition...")
        else:
            recogOn = True
            deactivateAndActivateBtn.mode = "main"
            deactivateAndActivateMode = "main"
            print("reactivated intruder recognition...")
        btnTimer += 1
    elif btnTimer >= btnTimerMax:
        btnTimer = 0
    else:
        btnTimer += 1


sliderValue = 1
leftOffset = 0
topOffset = 0
def zoomIn():
    global sliderValue
    if sliderValue >= 3:
        sliderValue = 3
    else:
        sliderValue += 0.01

def zoomOut():
    global sliderValue
    if sliderValue <= 1:
        sliderValue = 1
    else:
        sliderValue -= 0.01

def panDown():
    global topOffset
    if topOffset >= (camera_frame_height * sliderValue):
        topOffset = (camera_frame_height * sliderValue)
    else:
        topOffset += 1

def panUp():
    global topOffset
    if topOffset <= 0:
        topOffset = 0
    else:
        topOffset -= 1

def panRight():
    global leftOffset
    if leftOffset >= (camera_frame_width * sliderValue):
        leftOffset = (camera_frame_width * sliderValue)
    else:
        leftOffset += 1

def panLeft():
    global leftOffset
    if leftOffset <= 0:
        leftOffset = 0
    else:
        leftOffset -= 1

    

# -------- Main Program Loop -----------


while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # -- clear the screen
    screen.fill(ORANGEYRED)
 
    # -- put stuff on screen

    # background image
    bg = pygame.image.load('static/bg.png')
    bg = pygame.transform.scale(bg, (screen_width, screen_height))
    screen.blit(bg, (0, 0))

    # the camera footage
    if firstRun == True:
        result, firstRun, camOn, recogOn, cap,  face_cascade,  body_cascade,  detection,  detection_stopped_time, timer_started,  SECONDS_TO_RECORD_AFTER_DETECTION,  frame_size, fourcc, out = briesStuff(recording, firstRun, camOn, recogOn)
    else:
        result, firstRun, camOn, recogOn, cap,  face_cascade,  body_cascade,  detection,  detection_stopped_time, timer_started,  SECONDS_TO_RECORD_AFTER_DETECTION,  frame_size, fourcc, out = briesStuff(recording, firstRun, camOn, recogOn, cap,  face_cascade,  body_cascade,  detection,  detection_stopped_time, timer_started,  SECONDS_TO_RECORD_AFTER_DETECTION,  frame_size, fourcc, out)
    
    camera_frame_width = frame_size[0]
    camera_frame_height = frame_size[1]

    camera_left = (screen_width * 0.5) - (camera_frame_width * 0.5)
    camera_top = screen_height * 0.05
    
    show = (0, 0, camera_frame_width, camera_frame_height)

    if result != None:
        result = pygame.transform.scale(result, ((camera_frame_width * sliderValue),(camera_frame_height * sliderValue)))
        lastFrame = result
        screen.blit(result, (camera_left, camera_top), show)
    else:
        screen.blit(lastFrame, (camera_left, camera_top), show)

    # button for stop/start recording

    startAndStopBtn = Button(((screen_width * 0.5) - ((camera_frame_width * 0.16) * 0.5)), ((0.05 * screen_height) + camera_frame_height + (screen_height * 0.05)), (camera_frame_width * 0.16), ((screen_height - (screen_height * 0.05) - camera_frame_height) * 0.25), 'static/recording.png', "static/notRecording.png", "icon", startAndStop, startAndStopMode)
    buttons.append(startAndStopBtn)

    # button for deactivate/activate intruder recognition
    deactivateAndActivateBtn = Button(((screen_width * 0.5) - ((camera_frame_width * 0.16) * 0.5)), ((0.05 * screen_height) + camera_frame_height + (screen_height * 0.05) + ((screen_height - (screen_height * 0.05) - camera_frame_height) * 0.25) + (screen_height * 0.1)), (camera_frame_width * 0.16), ((screen_height - (screen_height * 0.05) - camera_frame_height) * 0.25), "static/sirenOn.png", "static/siren.png", "icon", deactivateAndActivate, deactivateAndActivateMode)
    buttons.append(deactivateAndActivateBtn)

    # button for zoom in    
    zoomInBtn = Button(((screen_width * 0.5) - (((camera_frame_width * 0.16) * 0.5) - (screen_width * 0.1))), ((0.05 * screen_height) + camera_frame_height + (screen_height * 0.05) + ((screen_height - (screen_height * 0.05) - camera_frame_height) * 0.25) + (screen_height * 0.01)), (camera_frame_width * 0.16), ((screen_height - (screen_height * 0.05) - camera_frame_height) * 0.25), "static/zoomIn.png", "static/zoomIn.png", "icon", zoomIn)
    buttons.append(zoomInBtn)

    # button for zoom out
    zoomOutBtn = Button(((screen_width * 0.5) - (((camera_frame_width * 0.16) * 0.5) + (screen_width * 0.1))), ((0.05 * screen_height) + camera_frame_height + (screen_height * 0.05) + ((screen_height - (screen_height * 0.05) - camera_frame_height) * 0.25) + (screen_height * 0.01)), (camera_frame_width * 0.16), ((screen_height - (screen_height * 0.05) - camera_frame_height) * 0.25), "static/zoomOut.png", "static/zoomOut.png", "icon", zoomOut)
    buttons.append(zoomOutBtn)

    

    # logo
    logo = pygame.image.load('static/logo.png')
    logo = pygame.transform.scale(logo, ((screen_width * 0.25), (screen_height * 0.2)))
    screen.blit(logo, ((screen_width - (screen_width * 0.26) - (screen_width * 0.005)), 0))



    for button in buttons:
        button.process(screen)
 
    # -- update the screen
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
    
    pressedKeys = pygame.key.get_pressed()
    if pressedKeys[pygame.K_ESCAPE]:
        done = True
 
# Close the window and quit.
pygame.quit()

