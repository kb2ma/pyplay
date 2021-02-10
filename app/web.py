# Copyright 2021, Ken Bannister
"""
Playing with web pages
"""
import logging
import re, requests
from threading import Thread

log = logging.getLogger(__name__)


def readWebPage():
    """Downloads and prints http://cytheric.net/index.html"""
    r = requests.get('http://cytheric.net/index.html')

    matches = re.findall('<([/]*)(\w+)(.*?)([/]*)>', r.text)
    tagCounts = {}
    print("Found {} tags".format(len(matches)))

    tags = set()
    for m in matches:
        #print(m)
        if (m[1] in tags) and m[0]:
            print("(end) {}".format(m[1]))
        else:
            tags.add(m[1])
            print(m[1])

#
# Functions for downloading multiple files, including threading
#

def _downloadFile(url):
    r = requests.get(url)
    fname = str.split(url, '/')[-1]
    isText = (str.split(fname, '.')[-1] == 'html')
    print("Retrieved {}, {} bytes".format(fname,
                                          len(r.text) if isText else len(r.content)))

def downloadFiles():
    """Downloads a few files, concurrently via threading"""
    prefix = 'http://cytheric.net'
    files = ['resume.pdf', 'index.html']

    for f in files:
        t = Thread(target=_downloadFile, args=(prefix + '/' + f,))
        t.start()
