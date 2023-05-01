####################################################################################
# Team Name: Texas Toast
# Members: Ryan Saffel, Brie Bays, Austin Newsom, Elora Browning
# Date: 4/19/2023
# Description: Hidden Security Camera
###################################################################################

# Austin Newsom
# Circuitry Component for PiCamera 

import RPi.GPIO as GPIO
from time import sleep

# set the LEDD and switch pin numbers
greenled = 17
greenbutton = 25

blueled = 13
bluebutton = 27

redled = 23
redbutton = 6  

# use the Broadcom pin mode
GPIO.setmode(GPIO.BCM)

# setup the LED and switch pns
GPIO.setup(greenled, GPIO.OUT)
GPIO.setup(greenbutton, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(blueled, GPIO.OUT)
GPIO.setup(bluebutton, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    
    # do this forever
    while (True):
        # light the LED when the switch is pressed
        # turn it off otherwise
        if (GPIO.input(greenbutton) == GPIO.HIGH):
            GPIO.output(greenled, GPIO.HIGH)
            print("Security System Is Active")
        else:
            GPIO.output(greenled, GPIO.LOW)
        
        if (GPIO.input(bluebutton) == GPIO.HIGH):
            GPIO.output(blueled, GPIO.HIGH)
            print("Click the Red Button to disable the circuit system")
        else:
            GPIO.output(blueled, GPIO.LOW)
        
        sleep(0.1)
        
except KeyboardInterrupt:
    GPIO.cleanup()




