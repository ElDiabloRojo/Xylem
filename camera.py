#!/usr/bin/python3

from picamera import PiCamera
from time import strftime 

timeString = strftime('%Y%m%d-%H%M%S')
outFile = '/home/pi/Pictures/phyto/' + timeString + '.jpg'

camera = PiCamera()
camera.resolution = (2592, 1944)

camera.capture(outFile)
