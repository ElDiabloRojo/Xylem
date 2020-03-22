import click
import os
from picamera import PiCamera
from time import strftime

timeString = strftime('%Y%m%d-%H%M%S')
outFile = dest + timeString + '.jpg'

@click.command()
@click.option("-d", "--dest", default=os.environ['PHYTO_IMG_DIR'], required=True, help="destination directory for image")
def cli(dest):
    """saves photo from rPi camera to specified directory."""
    timeString = strftime('%Y%m%d-%H%M%S')
    outFile = dest + timeString + '.jpg'

    camera = PiCamera()
    camera.resolution = (2592, 1944)
    camera.capture(outFile)
