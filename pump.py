#!/usr/bin/python3

from adafruit_motorkit import MotorKit
from time import sleep

def pump(seconds, direction):
    kit.motor1.throttle = direction
    sleep(seconds)

kit = MotorKit()
print('beginning feed')
print('filling feed tank')
pump(600, -1)
print('draining feed tank')
pump(600, 1)
print('ending feed')
pump(0, 0)
