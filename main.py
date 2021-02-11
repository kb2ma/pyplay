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
import app.files, app.net, app.web, websrv
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
    parser.add_argument('-m', '--multi_dl',
                        help="download multiple files concurrently",
                        action='store_true')
    parser.add_argument('-s', '--echo_server',
                        help="setup echo server",
                        action='store_true')
    parser.add_argument('-c', '--echo_client', help="run echo client with text")
    parser.add_argument('-k', '--web_server', help="run Flask web server on port 5000",
                        action='store_true')
    args = parser.parse_args()
    
    try:
        if args.file:
            app.files.parseFile(args.file)
        elif args.web_page:
            app.web.readWebPage()
        elif args.multi_dl:
            app.web.downloadFiles()
        elif args.echo_server:
            app.net.startServer()
        elif args.echo_client:
            app.net.runClient(args.echo_client.encode('utf-8'))
        elif args.web_server:
            websrv.run()
        else:
            print("No argument provided")
    except KeyboardInterrupt:
        pass
    except:
        log.exception("Catch-all handler for pyplay app")
        print("\nAborting; see log for exception.")
