#!/bin/python3

from argparse import ArgumentParser


def create_parser():
    parser = ArgumentParser(description="""
    accept configuration for pumping sequence
    """)

    parser.add_argument("--motor-list",
                        help="list of motor numbers to activate.",
                        nargs='+',
                        required=True)
    parser.add_argument("--feed-time",
                        help="length of time to run pump. (seconds)",
                        nargs=1,
                        required=True)

    return parser