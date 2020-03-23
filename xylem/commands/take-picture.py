import click
import os
from picamera import PiCamera
from time import strftime
import sys, os, glob, time
from boto.s3.connection import S3Connection
from boto.s3.key import Key


@click.command()
@click.option("-t", "--target", default=os.environ['PHYTO_IMG_DIR'], required=True, help="destination directory for image")
@click.option("-s", "--s3upload", default=False)

def s3_conf(target):
    AWS_ACCESS = os.environ['AWS_ACCESS']
    AWS_SECRET = os.environ['AWS_SECRET']
    conn = S3Connection(AWS_ACCESS,AWS_SECRET)
    bucket = conn.get_bucket('phyto-img')
    directory = target

    return AWS_ACCESS,AWS_SECRET,conn,bucket,directory

def percent_cb(complete, total):
    sys.stdout.write('.')
    sys.stdout.flush()

def getFiles(dir):
    return [os.path.basename(x) for x in glob.glob(str(dir) + '*.jpg')]

def upload_S3(dir, file):
    k = Key(bucket)
    k.key = f
    k.set_contents_from_filename(dir + f, cb=percent_cb, num_cb=10)

def removeLocal(dir, file):
    os.remove(dir + file)

def cli(target, s3upload):
    """saves photo from rPi camera to specified directory."""
    timeString = strftime('%Y%m%d-%H%M%S')
    outFile = dest + timeString + '.jpg'

    camera = PiCamera()
    camera.resolution = (2592, 1944)
    camera.capture(outFile)

    if s3upload:
        s3_conf(target)
        filenames = getFiles(directory)
        print(filenames)

        for f in filenames:
            print('rnUploading %s to s3 %s' % (f, bucket))
            upload_S3(directory, f)
            removeLocal(directory, f)
