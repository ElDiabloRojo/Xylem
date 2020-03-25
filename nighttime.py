#!/usr/bin/python3

import RPi.GPIO as gpio


def setup(relay):
    gpio.setmode(gpio.BCM)
    gpio.setup(relay, gpio.OUT)


def daytime(relay):
    gpio.output(relay, gpio.HIGH)

relay = 13
setup(relay)
print('daytime')
daytime(relay)
