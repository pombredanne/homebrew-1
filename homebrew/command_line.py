# -*- coding: utf-8 -*-
import argparse
import asyncio

from .homebrew import HomeBrew


def main():
    argparse.ArgumentParser(description='Get homebrew info').parse_args()

    event_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(event_loop)
    try:
        HomeBrew(event_loop).log_info()
    finally:
        event_loop.close()
