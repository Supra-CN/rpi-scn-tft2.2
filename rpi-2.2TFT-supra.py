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

import RPi.GPIO as GPIO
import socket
from enum import Enum
import gpiozero
from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero.pins.mock import MockFactory
import signal
import requests

pin_factory = None
GPIO.setmode(GPIO.BCM)

# pin_factory = MockFactory()

# pin_factory=PiGPIOFactory(host='172.24.115.124')
# pin_factory="172.24.115.124"

def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip


class Btn(Enum):
    TRIGON = gpiozero.Button(24, pin_factory=pin_factory)
    X = gpiozero.Button(5, pin_factory=pin_factory)
    CIRCLE = gpiozero.Button(23, pin_factory=pin_factory)
    SQUARE = gpiozero.Button(22, pin_factory=pin_factory)
    L = gpiozero.Button(17, pin_factory=pin_factory)
    # R = gpiozero.Button(4, pin_factory=pin_factory)


def on_btn_pressed(gbtn: gpiozero.Button):
    print("on Btn pressed: " + str(gbtn.pin))

    if gbtn == Btn.X.value:
        on_btn_x()
    elif gbtn == Btn.CIRCLE.value:
        on_btn_o()
    elif gbtn == Btn.SQUARE.value:
        on_btn_d()
    else:
        on_btn_no_impl()


def on_btn_no_impl():
    print("no impl")


def on_btn_o():
    ip = get_host_ip()
    print("ip: " + ip)
    params = {'host': ip}
    r = requests.get("http://rpi.supra.tw/update.php", params=params)
    print(r)

def on_btn_x():
    GPIO.setup(27, GPIO.OUT)
    print("screen off")

def on_btn_d():
    GPIO.setup(27, GPIO.IN)
    print("screen on")


for btn in Btn:
    btn.value.when_pressed = on_btn_pressed

# on_x()

print('listen for key event...')
signal.pause()
