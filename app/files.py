# Copyright 2021, Ken Bannister
"""
Playing with files
"""
import logging
log = logging.getLogger(__name__)


def parseFile(fname):
    """Prints the provided file, line by line"""
    for line in open(fname):
        print(line, end='')
