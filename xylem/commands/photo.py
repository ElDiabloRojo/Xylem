import click
from picamera import PiCamera
from time import strftime
import sys, os, glob, time
from boto.s3.connection import S3Connection
from boto.s3.key import Key


PHYTO_IMG_DIR = os.environ['PHYTO_IMG_DIR']
AWS_ACCESS = os.environ['AWS_ACCESS']
AWS_SECRET = os.environ['AWS_SECRET']

def percent_cb(complete, total):
    sys.stdout.write('.')
    sys.stdout.flush()

def getFiles(dir):
    return [os.path.basename(x) for x in glob.glob(str(dir) + '*.jpg')]

def upload_S3(bucket, dir, file):
    k = Key(bucket)
    k.key = file
    k.set_contents_from_filename(dir + file, cb=percent_cb, num_cb=10)

def removeLocal(dir, file):
    os.remove(dir + file)

@click.group()
def cli():
    pass

@cli.command()
@click.option(
        "-d",
        "--dest",
        default=PHYTO_IMG_DIR,
        required=True,
        help="destination directory for image"
    )
def take(dest):
    """saves photo from rPi camera to specified directory."""
    timeString = strftime('%Y%m%d-%H%M%S')
    outFile = dest + timeString + '.jpg'

    camera = PiCamera()
    camera.resolution = (2592, 1944)
    print('picture taken: %s' % outFile)
    camera.capture(outFile)

@cli.command()
@click.option(
        "-s",
        "--source",
        default=PHYTO_IMG_DIR,
        required=True,
        help="source directory for images"
    )
def upload(source):
    """uploads photos from specified source directory to s3."""
    conn = S3Connection(AWS_ACCESS, AWS_SECRET)
    bucket = conn.get_bucket('phyto-img')
    filenames = getFiles(source)
    print(filenames)

    for f in filenames:
        print('rnUploading %s to s3 %s' % (f, bucket))
        upload_S3(bucket, source, f)
        removeLocal(source, f)
