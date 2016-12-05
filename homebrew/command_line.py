# -*- coding: utf-8 -*-
import argparse
import asyncio

from homebrew import __version__

from .homebrew import HomeBrew


def main():
    parser = argparse.ArgumentParser(description='Get homebrew info')
    parser.add_argument('-v', '--version',
                        action='version', version=__version__)
    parser.parse_args()

    event_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(event_loop)
    try:
        HomeBrew(event_loop).log_info()
    finally:
        event_loop.close()
