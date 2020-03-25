import click
import RPi.GPIO as gpio
import sys, os, glob, time


RELAY = 13

def setup(relay):
    gpio.setmode(gpio.BCM)
    gpio.setup(relay, gpio.OUT)


def daytime(relay):
    gpio.output(relay, gpio.HIGH)

@click.command()
@click.option("-s", "--switch", required=True, help="provide values 'on' or 'off' to toggle ligth GPIO pin.")
def cli(switch):
    setup(RELAY)
    if switch == 'on':
        gpio.output(RELAY, gpio.LOW)
    elif switch == 'off':
        gpio.output(RELAY, gpio.HIGH)
    else:
        print('invalid input value')

