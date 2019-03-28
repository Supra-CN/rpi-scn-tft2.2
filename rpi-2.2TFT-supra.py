#!/usr/bin/env python3

""" rpi-2.2TFT-supra.py by supra 2019.03.2
GPIO Keyboard driver for Raspberry Pi 2.2TFT for use with 5 Buttons
requires uinput kernel module (sudo modprobe uinput)
requires python-uinput (git clone https://github.com/tuomasjjrasanen/python-uinput)
requires python RPi.GPIO (from http://pypi.python.org/pypi/RPi.GPIO/)

Steps:

1.Install the python lib
$sudo apt-get update
$sudo apt-get install libudev-dev
$sudo apt-get install python-pip
$sudo pip install rpi.gpio
$sudo pip install python-uinput

2. Perform the command
$sudo modprobe uinput

3. Perform the demo python program
$sudo ./rpi-2.2TFT-supra.py

"""

import time
from enum import Enum

# import RPi.GPIO as GPIO
import gpiozero
from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero.pins.mock import MockFactory
import signal

# GPIO.setmode(GPIO.BCM)

pin_factory=None
# pin_factory = MockFactory()


# pin_factory=PiGPIOFactory(host='172.24.115.124')
# pin_factory="172.24.115.124"

class Btn(Enum):
    TRIGON = gpiozero.Button(24, pin_factory=pin_factory)
    X = gpiozero.Button(5, pin_factory=pin_factory)
    CIRCLE = gpiozero.Button(23, pin_factory=pin_factory)
    SQUARE = gpiozero.Button(22, pin_factory=pin_factory)
    L = gpiozero.Button(17, pin_factory=pin_factory)
    R = gpiozero.Button(4, pin_factory=pin_factory)


def onBtnPressed(gbtn: gpiozero.Button):
    print("on Btn pressed: "+ str(gbtn.pin))

for btn in Btn:
    btn.value.when_pressed = onBtnPressed

print('listen for key event...')
signal.pause()

# setup GPIO
# GPIO.setup(Btn.TRIGON.value, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Trigon Button for GPIO24
# GPIO.setup(Btn.X.value, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # X Button for GPIO5
# GPIO.setup(Btn.CIRCLE.value, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Circle Button for GPIO23
# GPIO.setup(Btn.SQUARE.value, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Square Button for GPIO22
# GPIO.setup(Btn.L.value, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # L Button for GPIO17
# GPIO.setup(Btn.R.value, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # R Button for GPIO4

# events = (uinput.KEY_UP, uinput.KEY_DOWN, uinput.KEY_LEFT, uinput.KEY_RIGHT, uinput.KEY_LEFTCTRL)


#
# pressed = set()
#
# while True:
#     for btn in set(pressed):
#         if GPIO.input(btn.value):
#             print("relesed btn: " + str(btn) + " in pressed: " + str(pressed))
#             pressed.remove(btn)
#
#     if pressed:
#         continue
#
#     for btn in Btn:
#         if not GPIO.input(btn.value):
#             pressed.add(btn)
#             print("pressed btn: "+str(btn)+ " to pressed: " + str(pressed))
#
#     time.sleep(0.04)
#     # time.sleep(1)
