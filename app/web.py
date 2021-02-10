# Copyright 2021, Ken Bannister
"""
Playing with web pages
"""
import logging
import queue, re, requests
from threading import Thread, Lock

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

# Tracks when all files have been retrieved
fileQ = queue.Queue()
dlSum = 0
sumLock = Lock()

def _downloadFile(fileQ):
    global dlSum

    url = fileQ.get()
    r = requests.get(url)
    fname = str.split(url, '/')[-1]
    isText = (str.split(fname, '.')[-1] == 'html')
    dlSize = len(r.text) if isText else len(r.content)
    
    print("Retrieved {}, {} bytes".format(fname, dlSize))
    with sumLock:
        dlSum += dlSize
    fileQ.task_done()

def downloadFiles():
    """Downloads a few files, concurrently via threading. Waits for all to
       finish.
    """
    prefix = 'http://cytheric.net'
    files = ['resume.pdf', 'index.html']

    for f in files:
        fileQ.put(prefix + '/' + f)
        t = Thread(target=_downloadFile, args=(fileQ,))
        t.start()

    fileQ.join()
    print("\nAll files retrieved; {} bytes".format(dlSum))
