""" rpi-2.2TFT-kbrd.py by ukonline2000 2015.12.08
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
$sudo python rpi-2.2TFT-kbrd.py

"""



import uinput
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

btn_trigon = 24
btn_x = 5
btn_circle = 23
btn_square = 22
btn_l = 17
btn_r = 4

# Up, Down, left, right, fire
GPIO.setup(btn_trigon, GPIO.IN, pull_up_down=GPIO.PUD_UP)  #Trigon Button for GPIO24
GPIO.setup(btn_x, GPIO.IN, pull_up_down=GPIO.PUD_UP)  #X Button for GPIO5
GPIO.setup(btn_circle, GPIO.IN, pull_up_down=GPIO.PUD_UP)  #Circle Button for GPIO23
GPIO.setup(btn_square, GPIO.IN, pull_up_down=GPIO.PUD_UP)  #Square Button for GPIO22
GPIO.setup(btn_l, GPIO.IN, pull_up_down=GPIO.PUD_UP)  #L Button for GPIO17
GPIO.setup(btn_r, GPIO.IN, pull_up_down=GPIO.PUD_UP)  #R Button for GPIO4

events = (uinput.KEY_UP, uinput.KEY_DOWN, uinput.KEY_LEFT, uinput.KEY_RIGHT, uinput.KEY_LEFTCTRL)

# device = uinput.Device(events)

while True:
  if not GPIO.input(btn_r):  # Fire button pressed
    print('r')
  if not GPIO.input(btn_trigon):  # Up button pressed
    print('t')
  if not GPIO.input(btn_x):  # Down button pressed
    print('x')
  if not GPIO.input(btn_l):  # Left button pressed
    print('l')
  if not GPIO.input(btn_square):  # Right button pressed
    print('s')
  if not GPIO.input(btn_circle):  # Right button pressed
    print('c')
  time.sleep(.04)
