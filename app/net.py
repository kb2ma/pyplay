# Copyright 2021, Ken Bannister
"""
Playing with network client/server
"""
import logging
from socketserver import BaseRequestHandler, TCPServer
from socket import socket, AF_INET, SOCK_STREAM

log = logging.getLogger(__name__)


class EchoHandler(BaseRequestHandler):
    """Handler to reflect request text back to echo client"""
    def handle(self):
        print("Got connection from", self.client_address)
        while True:
            msg = self.request.recv(8192)
            if not msg:
                break
            self.request.send(msg)

def startServer():
    """Start echo server"""
    s = TCPServer(('', 10000), EchoHandler)
    print("Server runs indefinitely; Ctrl-C to exit")
    s.serve_forever()

def runClient(text):
    """Client sends the provided text to the server"""
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(('localhost', 10000))

    s.send(text)
    print(s.recv(8192))
