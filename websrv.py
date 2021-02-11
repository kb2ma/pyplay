# Copyright 2021, Ken Bannister
"""
Simple Flask web server
"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hi Mom!</h1>'

def run():
    app.run()
