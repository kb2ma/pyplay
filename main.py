#!/usr/bin/env python3
# Copyright 2021, Ken Bannister
"""
Entry point for pyplay app. Includes exercises for common tool tasks, like read
a file or retrieve a web page.

To see command details:
   $. ./main.py -h
"""
import logging, sys
import re, requests
import app.files, app.web
logging.basicConfig(filename='pyplay.log', level=logging.DEBUG, 
                    format='%(asctime)s %(module)s %(message)s')
log = logging.getLogger(__name__)


# Start from command line
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help="file to parse")
    parser.add_argument('-w', '--web_page', help="read web page",
                        action='store_true')
    parser.add_argument('-c', '--concurrent',
                        help="download multiple files concurrently",
                        action='store_true')
    args = parser.parse_args()
    
    try:
        if args.file:
            app.files.parseFile(args.file)
        elif args.web_page:
            app.web.readWebPage()
        elif args.concurrent:
            app.web.downloadFiles()
        else:
            print("No argument provided")
    except KeyboardInterrupt:
        pass
    except:
        log.exception("Catch-all handler for balena app")
        print("\nAborting; see log for exception.")
