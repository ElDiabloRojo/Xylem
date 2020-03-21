#!/usr/bin/python3

import RPi.GPIO as gpio
from time import sleep


def setup(relay):
    gpio.setmode(gpio.BCM)
    gpio.setwarnings(False)
    gpio.setup(relay, gpio.OUT)

def oxygenate(relay, seconds):
    gpio.output(relay, gpio.HIGH)
    sleep(seconds)
    gpio.output(relay, gpio.LOW)

relay = 12 
print('beginning air pump sequence')
print('setting up IO pins')
setup(relay)
print('oxygenate water supply')
oxygenate(relay, 600)
