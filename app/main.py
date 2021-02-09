#!/usr/bin/env python3
# Copyright 2021, Ken Bannister
"""
Entry point for balena app. Includes exercises for common tool tasks, like read
a file or retrieve a web page.

To see command details:
   $. ./main.py -h
"""
import logging, sys
import re, requests
logging.basicConfig(filename='balena.log', level=logging.DEBUG, 
                    format='%(asctime)s %(module)s %(message)s')
log = logging.getLogger(__name__)


def parseFile(fname):
    """Prints the provided file, line by line"""
    for line in open(fname):
        print(line, end='')

def readWebPage():
    """Downloads and prints http://cytheric.net/index.html"""
    r = requests.get('http://cytheric.net/index.html')

    matches = re.findall('<([/]*)(\w+)(.*?)([/]*)>', r.text)
    tagCounts = {}
    print("Found {} tags".format(len(matches)))

    tag = ''
    for m in matches:
        if m[1] == tag and m[0]:
            print("Found matching tag for {}".format(m[1]))
        else:
            tag = m[1]
            print(m[1])

    #with open('cytheric-index.html', 'w') as f:
    #    f.write(r.text)
    #log.info("Wrote cytheric-index.html")
    

# Start from command line
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help="file to parse")
    parser.add_argument('-w', '--web_page', help="web page to read",
                        action='store_true')
    args = parser.parse_args()
    
    try:
        if args.file:
            parseFile(args.file)
        elif args.web_page:
            readWebPage()
        else:
            print("No argument provided")
    except KeyboardInterrupt:
        pass
    except:
        log.exception("Catch-all handler for balena app")
        print("\nAborting; see log for exception.")
