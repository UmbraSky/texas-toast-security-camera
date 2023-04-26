####################################################################################
# Team Name: Texas Toast
# Members: Ryan Saffel, Brie Bays, Austin Newsom, Elora Browning
# Date: 4/19/2023
# Description: Hidden Security Camera
###################################################################################

# Austin Newsom
# Circuitry Component for PiCamera 

# Notes to Self: Create Diagram for Circuit 
#                Possibly Enable an alarm system


# Code that will activate the green light whenever the program begins running

    # Print message to the terminal saying "Program Started"

    # Code to play a sound when green light activates

    # Code for when the green button is pushed

        # "Manual System Restart" message when button is pushed

# Code that will activate the red light when invalid user input is given (invalid spelling error, unknown command)

    # Print help message to the terminal when invalid input is given 
    # "Invalid Input given, command is either unknown or spelled incorrectly. Please give a valid input"

    # Code to play a sound when red light activates

# Code that will consistently run the blue right while the program is active

    # Print message to the terminal intermittently saying the program is in "Idle Mode"

    # Code to play a sound when blue light is active

# Code that will activate the yellow light when someone pushes the button
     
     # Print message to the terminal "Are you sure you want to terminate the program?"

     # Yellow Light Code stops running if answer is not given in time, but if button is clicked again, program stops
    
    
# Start of Code:

import RPi.GPIO as GPIO
import time
import sys
import signal
import json

greenled =                           # add corresponding led numbers
redled =
blueled =
yellowled =

leds = [greenled, redled, blueled, yellowled]

greenButton =                       # add corresponding button numbers
redButton =
blueButton =
yellowButton =

buttons = [greenButton, redButton, blueButton, yellowButton]

GPIO.setmode(GPIO.BCM)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(buttons, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    if (GPIO.input(greenButton) == GPIO.HIGH):
        GPIO.output(greenled, GPIO.HIGH)
        print("System Restarting...")
    else:
        GPIO.output(greenled, GPIO.LOW)
        
    if (GPIO.input(redButton) == GPIO.HIGH):
        GPIO.output(redled, GPIO.HIGH)
    else:
        GPIO.output(redled, GPIO.LOW)
        
    if (GPIO.input(blueButton) == GPIO.HIGH):
        GPIO.output(blueled, GPIO.HIGH)
    else:
        GPIO.output(blueled, GPIO.LOW)
        
    if (GPIO.input(yellowButton) == GPIO.HIGH):
        GPIO.output(yellowled, GPIO.HIGH)
        print("Are you sure you want to terminate the system?")
    else:
        GPIO.output(yellowled, GPIO.LOW)
        




