import pygame
import RPi.GPIO as GPio

GPio.setmode(GPio.BCM)
GPio.setup(18, GPio.OUT)  # Motor 1 Pin 1
GPio.setup(23, GPio.OUT)  # Motor 1 Pin 2
GPio.setup(24, GPio.OUT)  # Motor 2 Pin 1
GPio.setup(25, GPio.OUT)  # Motor 2 Pin 2

pygame.init()

joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
dualsense = None
for joystick in joysticks:
    if joystick.get_name() == "PS5 Controller":
        dualsense = joystick
        dualsense.init()
        break

def control_motors():
    # Get the D-pad button states
    dpad_up = dualsense.get_button(0)
    dpad_down = dualsense.get_button(1)
    dpad_left = dualsense.get_button(2)
    dpad_right = dualsense.get_button(3)
    
    # Control Motor 1
    if dpad_up:
        GPIO.output(18, GPIO.HIGH)
        GPIO.output(23, GPIO.LOW)
    elif dpad_down:
        GPIO.output(18, GPIO.LOW)
        GPIO.output(23, GPIO.HIGH)
    else:
        GPIO.output(18, GPIO.LOW)
        GPIO.output(23, GPIO.LOW)
    
    # Control Motor 2
    if dpad_right:
        GPIO.output(24, GPIO.HIGH)
        GPIO.output(25, GPIO.LOW)
    elif dpad_left:
        GPIO.output(24, GPIO.LOW)
        GPIO.output(25, GPIO.HIGH)
    else:
        GPIO.output(24, GPIO.LOW)
        GPIO.output(25, GPIO.LOW)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            GPIO.cleanup()
            quit()
    
    control_motors()
