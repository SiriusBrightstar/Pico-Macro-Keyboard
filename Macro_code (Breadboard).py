# Rename this file as code.py and save to the Raspberry Pi Pico
# This code is configured to send GTA Vice City cheat codes on press of a button

import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

A = 'aspirine'
B = 'preciousprotection'
C = 'leavemealone'
D = 'gettherefast'
E = 'nuttertools'

kbd = Keyboard(usb_hid.devices)             #Initialize Pico as a HID Keyboard Device
layout = KeyboardLayoutUS(kbd)

LED = digitalio.DigitalInOut(board.GP25)    #Initialize On-Board LED
LED.direction = digitalio.Direction.OUTPUT

BT1 = digitalio.DigitalInOut(board.GP15)    #Set GPIO 15 as Button 1
BT1.direction = digitalio.Direction.INPUT   #Set GPIO 15 as Input 
BT1.pull = digitalio.Pull.DOWN              #Set GPIO 15 as Active HIGH, meaning GP15 is LOW & to be 
                                            #triggered 3.3v needs to be connected. 

BT2 = digitalio.DigitalInOut(board.GP14)    #Set GPIO 14 as Button 
BT2.direction = digitalio.Direction.INPUT
BT2.pull = digitalio.Pull.DOWN

BT3 = digitalio.DigitalInOut(board.GP13)    #Set GPIO 13 as Button 
BT3.direction = digitalio.Direction.INPUT
BT3.pull = digitalio.Pull.DOWN

BT4 = digitalio.DigitalInOut(board.GP12)    #Set GPIO 12 as Button 
BT4.direction = digitalio.Direction.INPUT
BT4.pull = digitalio.Pull.DOWN

BT5 = digitalio.DigitalInOut(board.GP11)    #Set GPIO 11 as Button 
BT5.direction = digitalio.Direction.INPUT
BT5.pull = digitalio.Pull.DOWN

while True:                                 #Infinite Loop
    if BT1.value == True:
        layout.write(A)                     #Add text to be triggered by GP15
        LED.value = True                    #LED turns on for 0.1s when Button is pressed
        time.sleep(0.3)
    elif BT2.value == True:
        layout.write(B)                     #Add text to be triggered by GP14
        LED.value = True
        time.sleep(0.3)
    elif BT3.value == True:
        layout.write(C)                     #Add text to be triggered by GP13
        LED.value = True
        time.sleep(0.3)
    elif BT4.value == True:
        layout.write(D)                     #Add text to be triggered by GP12
        LED.value = True
        time.sleep(0.3)
    elif BT5.value == True:
        layout.write(E)                     #Add text to be triggered by GP11
        LED.value = True
        time.sleep(0.3)
    LED.value = False
