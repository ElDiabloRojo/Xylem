#!/usr/bin/python3

import RPi.GPIO as gpio


def setup(relay):
    gpio.setmode(gpio.BCM)
    gpio.setup(relay, gpio.OUT)


def nighttime(relay):
    gpio.output(relay, gpio.LOW)

relay = 13
setup(relay)
print('nighttime')
nighttime(relay)
