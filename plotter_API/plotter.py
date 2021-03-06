import argparse
import os.path
import sys

def main(argv):
    """Program entry point.
    :param argv: command-line arguments
    :type argv: :class:`list`
    """

    parser = argparse.ArgumentParser(description='Clear profanity from the text.')
    parser.add_argument('input',
                        nargs=1,
                        type=argparse.FileType('r'),
                        help='Input file')
    parser.add_argument('output',
                        type=argparse.FileType('w'),
                        nargs=1,
                        help='Output destination')
    parser.add_argument('--type',
                        choices=['corpus', 'text'],
                        nargs='?',
                        help='Input file type (vert is corpus by default)')

    args = parser.parse_args(argv)

    

def entry_point():
    """Zero-argument entry point for use with setuptools/distribute."""

    raise SystemExit(main(sys.argv[1:]))


if __name__ == '__main__':
    entry_point()