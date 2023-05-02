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

# set the LED and switch pin numbers
led = 17 # blueLED
ledTwo = 13 #greenLED
ledThree = 6 #redLED
button = 25 #greenButton

# uses the Broadcom pin mode
GPIO.setmode(GPIO.BCM)

# setups the LEDs and switch pins
GPIO.setup(led, GPIO.OUT)
GPIO.setup(ledTwo, GPIO.OUT)
GPIO.setup(ledThree, GPIO.OUT)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    # blink the LED forever
    while (True):
    # the delay is 3s if the switch is not pressed
        if (GPIO.input(button) == GPIO.HIGH):
            delay = 3
            print("System Active")
        # otherwise, it's 0.25s
        elif (GPIO.input(button) == GPIO.LOW):
            delay = 0.25
            
        # blink the LED
        GPIO.output(led, GPIO.HIGH)
        GPIO.output(ledTwo, GPIO.HIGH)
        GPIO.output(ledThree, GPIO.HIGH)
        sleep(delay)
        GPIO.output(led, GPIO.LOW)
        GPIO.output(ledTwo,GPIO.LOW)
        GPIO.output(ledThree, GPIO.LOW)
        sleep(delay)
        
    # detect Ctrl+C
except KeyboardInterrupt:
    # reset the GPIO pins
    GPIO.cleanup()
