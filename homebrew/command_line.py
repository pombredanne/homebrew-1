import argparse

from homebrew import HomeBrew, __version__


def main():
    parser = argparse.ArgumentParser(description="Get homebrew info")
    parser.add_argument("-v", "--version", action="version", version=__version__)
    parser.parse_args()

    HomeBrew().info
