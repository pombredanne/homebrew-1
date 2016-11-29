# -*- coding: utf-8 -*-
import argparse

from .homebrew import HomeBrew


def main():
    argparse.ArgumentParser(description='Get homebrew info').parse_args()
    HomeBrew().log_info()
